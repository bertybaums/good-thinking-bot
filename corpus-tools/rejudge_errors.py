"""Re-judge rows with score=-1 in a benchmark jsonl, in place."""
import asyncio, json, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from benchmark import build_judge_prompt, load_anchors, JUDGE_MODEL, MINDROUTER_API_KEY, MINDROUTER_BASE_URL
import openai

anchors_by_id = {a["id"]: a for a in load_anchors()}
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
            parsed = json.loads(r.choices[0].message.content or "")
            row["score"] = int(parsed.get("score", 0))
            row["judge_reasoning"] = parsed.get("reasoning", "")
        except Exception as e:
            row["judge_reasoning"] = f"Re-judge error: {e}"
    return row

async def fix_file(path):
    rows = [json.loads(l) for l in open(path)]
    errs = [r for r in rows if r["score"] < 0]
    print(f"{path.name}: {len(errs)} errors")
    if not errs: return
    await asyncio.gather(*(judge(r) for r in errs))
    with open(path, "w") as f:
        for r in rows:
            f.write(json.dumps(r) + "\n")
    fixed = sum(1 for r in errs if r["score"] >= 0)
    print(f"  fixed {fixed}/{len(errs)}")

async def main():
    for p in sys.argv[1:]:
        await fix_file(Path(p))

asyncio.run(main())
