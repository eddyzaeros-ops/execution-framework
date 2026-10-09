import sys
import re

sys.stdout.reconfigure(encoding="utf-8")

with open("paper_raw.html", "r", encoding="utf-8") as f:
    html = f.read()

# Let's find all tables with id containing 'T'
tables = re.findall(r'<figure[^>]*id=["\']([^"\']*\.T\d+[^"\']*)["\'][^>]*>(.*?)</figure>', html, re.DOTALL)
print(f"Total tables found: {len(tables)}")
for tid, tcontent in tables:
    cap_m = re.search(r'<figcaption[^>]*>(.*?)</figcaption>', tcontent, re.DOTALL)
    caption = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', cap_m.group(1))).strip() if cap_m else "No caption"
    
    # count rows in table
    rows = re.findall(r'<tr[^>]*>.*?</tr>', tcontent, re.DOTALL)
    print(f"Table ID: {tid} | Rows: {len(rows)} | Caption: {caption[:90]}")
