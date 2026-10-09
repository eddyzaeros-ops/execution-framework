"""評估框架：對 RAG API 跑評估集，輸出指標與逐題結果。

用法：
  python eval/run_eval.py --dataset eval/datasets/doc_qa_v1.jsonl --api http://localhost:8080
      [--judge-url http://LLM:8000/v1 --judge-model domain-llm] [--tag baseline]
"""
import argparse
import json
import os
import re
import statistics
import time

import httpx
import yaml

NO_ANSWER = "文件中查無依據"

RUBRIC = (
    "你是嚴格的技術文件評審。依題目與參考答案，為受測回答評分，每項 1 到 5 分。\n"
    "correctness：數值、單位、條文是否正確。\n"
    "groundedness：是否只根據引用出處、沒有編造。\n"
    '只輸出 JSON，例如 {"correctness": 4, "groundedness": 5, "reason": "..."}'
)


def judge(url: str, model: str, item: dict, answer: str) -> dict:
    prompt = (f"題目：{item['question']}\n參考答案：{item.get('reference_answer') or '（無）'}\n"
              f"受測回答：{answer}")
    try:
        r = httpx.post(f"{url}/chat/completions", timeout=120, json={
            "model": model, "temperature": 0,
            "messages": [{"role": "system", "content": RUBRIC}, {"role": "user", "content": prompt}]})
        r.raise_for_status()
        text = r.json()["choices"][0]["message"]["content"]
        m = re.search(r"\{.*\}", text, re.S)
        return json.loads(m.group(0)) if m else {"error": "no json"}
    except Exception as e:  # 評審失敗不影響其他指標
        return {"error": str(e)}


def score_item(item: dict, resp: dict) -> dict:
    answer = resp.get("answer", "")
    retrieved = {s["doc_id"] for s in resp.get("retrieved", [])}
    cited = {s["doc_id"] for s in resp.get("sources", [])}
    expected = set(item.get("expected_sources", []))
    forbidden = set(item.get("forbidden_sources", []))
    is_no_answer = NO_ANSWER in answer

    res = {
        "id": item["id"], "user": item["user"], "tags": item.get("tags", []),
        "answer": answer, "retrieved": sorted(retrieved), "cited": sorted(cited),
        "latency_s": resp.get("latency_s"),
        # 越權：無權限文件出現在檢索或引用中
        "leak": bool(forbidden & (retrieved | cited)),
    }
    if item.get("expect_no_answer"):
        res["no_answer_ok"] = is_no_answer
    else:
        res["recall"] = len(expected & retrieved) / len(expected) if expected else None
        res["citation_ok"] = bool(cited) and cited <= expected if expected else None
        kws = item.get("must_include", [])
        res["keyword_cov"] = sum(k in answer for k in kws) / len(kws) if kws else None
        res["false_no_answer"] = is_no_answer
    return res


def _mean(vals):
    vals = [float(v) for v in vals if v is not None]
    return round(statistics.mean(vals), 3) if vals else None


def summarize(results: list[dict]) -> dict:
    lat = sorted(r["latency_s"] for r in results if r.get("latency_s") is not None)
    p = lambda q: lat[min(len(lat) - 1, int(q * len(lat)))] if lat else None
    judged = [r["judge"] for r in results if isinstance(r.get("judge"), dict) and "correctness" in r["judge"]]
    return {
        "n": len(results),
        "errors": sum(1 for r in results if r.get("error")),
        "leaks": sum(1 for r in results if r.get("leak")),
        "recall_at_k": _mean(r.get("recall") for r in results),
        "citation_accuracy": _mean(r.get("citation_ok") for r in results),
        "keyword_coverage": _mean(r.get("keyword_cov") for r in results),
        "no_answer_accuracy": _mean(r.get("no_answer_ok") for r in results),
        "false_no_answer_rate": _mean(r.get("false_no_answer") for r in results),
        "judge_correctness": _mean(j.get("correctness") for j in judged),
        "judge_groundedness": _mean(j.get("groundedness") for j in judged),
        "latency_p50_s": p(0.5), "latency_p95_s": p(0.95),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dataset", required=True)
    ap.add_argument("--api", default="http://localhost:8080")
    ap.add_argument("--users", default=os.path.join(os.path.dirname(__file__), "eval_users.yaml"))
    ap.add_argument("--judge-url")
    ap.add_argument("--judge-model", default="domain-llm")
    ap.add_argument("--tag", default=time.strftime("%Y%m%d-%H%M%S"))
    ap.add_argument("--out", default=os.path.join(os.path.dirname(__file__), "results"))
    args = ap.parse_args()

    keys = yaml.safe_load(open(args.users, encoding="utf-8"))
    items = [json.loads(l) for l in open(args.dataset, encoding="utf-8") if l.strip()]
    results = []
    with httpx.Client(timeout=300) as c:
        for item in items:
            try:
                r = c.post(f"{args.api}/ask", json={"question": item["question"]},
                           headers={"X-API-Key": keys[item["user"]]})
                r.raise_for_status()
                res = score_item(item, r.json())
                if args.judge_url and not item.get("expect_no_answer"):
                    res["judge"] = judge(args.judge_url, args.judge_model, item, res["answer"])
            except Exception as e:
                res = {"id": item["id"], "error": str(e)}
            results.append(res)
            flag = "LEAK!" if res.get("leak") else ("ERR" if res.get("error") else "ok")
            print(f"{item['id']:>6} {flag}")

    summary = summarize(results)
    os.makedirs(args.out, exist_ok=True)
    path = os.path.join(args.out, f"{args.tag}.json")
    json.dump({"tag": args.tag, "dataset": args.dataset, "summary": summary, "results": results},
              open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    print("結果：", path)
    if summary["leaks"]:
        print("警告：發現越權洩漏，請立即檢查權限設定")
        raise SystemExit(2)


if __name__ == "__main__":
    main()
