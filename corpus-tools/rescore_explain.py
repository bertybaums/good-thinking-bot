"""Re-score saved explain-mode subject responses after judge API key rotation."""
import asyncio, json, os, sys
from pathlib import Path
from collections import defaultdict

sys.path.insert(0, str(Path(__file__).parent))
from benchmark import build_judge_prompt, load_anchors, JUDGE_MODEL, MINDROUTER_API_KEY, MINDROUTER_BASE_URL
import openai

IN = Path(__file__).parent / "output/post-training/benchmark_gtb-qwen7b-qlora.jsonl"
OUT = Path(__file__).parent / "output/post-training/benchmark_gtb-qwen7b-qlora.rescored.jsonl"

anchors_by_id = {a["id"]: a for a in load_anchors()}
rows = [json.loads(l) for l in open(IN)]
print(f"Loaded {len(rows)} rows")

client = openai.AsyncOpenAI(api_key=MINDROUTER_API_KEY, base_url=MINDROUTER_BASE_URL)
sem = asyncio.Semaphore(4)

async def judge(row):
    anchor = anchors_by_id[row["id"]]
    prompt = build_judge_prompt(anchor, row["subject_response"], row["mode"])
    async with sem:
        try:
            r = await client.chat.completions.create(
                model=JUDGE_MODEL,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=200, temperature=0.1,
                extra_body={"chat_template_kwargs": {"enable_thinking": False}},
            )
            txt = r.choices[0].message.content or ""
            parsed = json.loads(txt)
            row["score"] = int(parsed.get("score", 0))
            row["judge_reasoning"] = parsed.get("reasoning", "")
        except Exception as e:
            row["score"] = -1
            row["judge_reasoning"] = f"Judge error: {e}"
    return row

async def main():
    done = 0
    tasks = [judge(r) for r in rows]
    results = []
    for coro in asyncio.as_completed(tasks):
        results.append(await coro)
        done += 1
        if done % 20 == 0:
            print(f"  {done}/{len(rows)}", flush=True)
    results.sort(key=lambda r: r["id"])
    with open(OUT, "w") as f:
        for r in results:
            f.write(json.dumps(r) + "\n")
    valid = [r for r in results if r["score"] >= 0]
    print(f"\nValid: {len(valid)}/{len(results)}")
    if valid:
        print(f"Mean explain: {sum(r['score'] for r in valid)/len(valid):.2f}/4")
        by_track = defaultdict(list)
        for r in valid: by_track[r["track"]].append(r["score"])
        print("\nBy track:")
        for t, v in sorted(by_track.items()):
            print(f"  {t:30s} {sum(v)/len(v):.2f}  n={len(v)}")

asyncio.run(main())
