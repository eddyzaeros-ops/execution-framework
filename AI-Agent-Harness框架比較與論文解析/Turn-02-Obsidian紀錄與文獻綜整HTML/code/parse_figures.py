import sys
import re

sys.stdout.reconfigure(encoding="utf-8")

with open("paper_raw.html", "r", encoding="utf-8") as f:
    html = f.read()

figs = re.findall(r'<figure[^>]*id=["\']([^"\']+)["\'][^>]*>(.*?)</figure>', html, re.DOTALL)
print(f"Total figures by id: {len(figs)}")
for fid, fcontent in figs:
    cap_match = re.search(r'<figcaption[^>]*>(.*?)</figcaption>', fcontent, re.DOTALL)
    cap = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', cap_match.group(1))).strip() if cap_match else "No caption"
    has_svg = "<svg" in fcontent
    print(f"ID: {fid} | SVG: {has_svg} | Cap: {cap[:110]}")
