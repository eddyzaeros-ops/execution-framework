"""比較兩次評估結果。用法：python eval/compare.py results/baseline.json results/new.json"""
import json
import sys

a, b = (json.load(open(p, encoding="utf-8")) for p in sys.argv[1:3])
print(f"{'指標':<24}{a['tag']:>16}{b['tag']:>16}{'差異':>10}")
for k, va in a["summary"].items():
    vb = b["summary"].get(k)
    diff = round(vb - va, 3) if isinstance(va, (int, float)) and isinstance(vb, (int, float)) else ""
    print(f"{k:<24}{str(va):>16}{str(vb):>16}{str(diff):>10}")
