"""Judge subagent responses on hard cases."""
import asyncio, json, sys, statistics
from pathlib import Path
from collections import defaultdict

sys.path.insert(0, str(Path(__file__).parent))
from benchmark import build_judge_prompt, load_anchors, JUDGE_MODEL, MINDROUTER_API_KEY, MINDROUTER_BASE_URL
import openai

anchors_by_id = {a["id"]: a for a in load_anchors()}
client = openai.AsyncOpenAI(api_key=MINDROUTER_API_KEY, base_url=MINDROUTER_BASE_URL)
sem = asyncio.Semaphore(4)

# For classify mode, follow benchmark.py logic: mechanical letter-match (the response IS the code).
# But the build_judge_prompt expects subject_response text. Actually benchmark.py scores classify
# mechanically (predicted vs correct taxonomy_code). Let me replicate that.

def classify_score(row):
    a = anchors_by_id[row["id"]]
    correct = a["taxonomy_code"]
    predicted = row["subject_response"].strip()
    return (4 if predicted == correct else 0), f"Predicted: {predicted}, Correct: {correct}"

async def judge_explain(row):
    anchor = anchors_by_id[row["id"]]
    prompt = build_judge_prompt(anchor, row["subject_response"], row["mode"])
    async with sem:
        r = await client.chat.completions.create(
            model=JUDGE_MODEL,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300, temperature=0.1,
            extra_body={"chat_template_kwargs": {"enable_thinking": False}},
        )
        try:
            parsed = json.loads(r.choices[0].message.content or "")
            return int(parsed.get("score", 0)), parsed.get("reasoning", "")
        except Exception as e:
            return -1, f"Parse error: {e}"

async def main():
    rows = [json.loads(l) for l in open(Path(__file__).parent / "output/subagent_responses.jsonl")]
    out = []
    explain_tasks = []
    for r in rows:
        if r["mode"] == "classify":
            score, why = classify_score(r)
            out.append({**r, "score": score, "judge_reasoning": why})
        else:
            explain_tasks.append(r)
    judged = await asyncio.gather(*(judge_explain(r) for r in explain_tasks))
    for r, (score, why) in zip(explain_tasks, judged):
        out.append({**r, "score": score, "judge_reasoning": why})
    out_path = Path(__file__).parent / "output/subagent_judged.jsonl"
    with open(out_path, "w") as f:
        for r in out: f.write(json.dumps(r) + "\n")

    # Compare to baseline
    print(f"\n{'ID':15s} {'mode':9s} {'subagent':>9s} {'base_mean':>9s} {'base_max':>9s} delta")
    print("-"*70)
    import glob
    files = glob.glob(str(Path(__file__).parent / "output/benchmark_*.jsonl")) + [str(Path(__file__).parent / "output/post-training/benchmark_gtb-qwen7b-qlora.rescored.jsonl")]
    base = defaultdict(list)
    for f in files:
        for l in open(f):
            r = json.loads(l)
            if r["score"] >= 0:
                base[(r["id"], r["mode"])].append(r["score"])
    for r in sorted(out, key=lambda x: (x["mode"], x["id"])):
        b = base.get((r["id"], r["mode"]), [])
        bm = statistics.mean(b) if b else float('nan')
        bx = max(b) if b else 0
        delta = r["score"] - bm if b else 0
        print(f"{r['id']:15s} {r['mode']:9s} {r['score']:>9d} {bm:>9.2f} {bx:>9d} {delta:+.2f}")

    # Aggregate
    sub_explain = [r["score"] for r in out if r["mode"]=="explain" and r["score"]>=0]
    sub_classify = [r["score"] for r in out if r["mode"]=="classify"]
    print(f"\nSubagent explain mean (n={len(sub_explain)}): {sum(sub_explain)/len(sub_explain):.2f}")
    print(f"Subagent classify mean (n={len(sub_classify)}): {sum(sub_classify)/len(sub_classify):.2f}")

asyncio.run(main())
