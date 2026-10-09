import sys
import re

sys.stdout.reconfigure(encoding="utf-8")

with open("paper_raw.html", "r", encoding="utf-8") as f:
    html = f.read()

def clean_cell(cell_html):
    # remove tags
    text = re.sub(r'<[^>]+>', ' ', cell_html)
    # clean math or symbols
    text = text.replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>').replace('&quot;', '"')
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def parse_html_table(t_html):
    rows = []
    # check thead / tbody or direct tr
    tr_matches = re.findall(r'<tr[^>]*>(.*?)</tr>', t_html, re.DOTALL)
    for tr in tr_matches:
        cells = re.findall(r'<t[hd][^>]*>(.*?)</t[hd]>', tr, re.DOTALL)
        if cells:
            clean_row = [clean_cell(c) for c in cells]
            rows.append(clean_row)
    return rows

table_blocks = re.findall(r'<figure[^>]*id=["\']([^"\']*\.T\d+[^"\']*)["\'][^>]*>(.*?)</figure>', html, re.DOTALL)
print(f"Parsing {len(table_blocks)} tables...")

all_parsed_tables = {}
for tid, content in table_blocks:
    cap_m = re.search(r'<figcaption[^>]*>(.*?)</figcaption>', content, re.DOTALL)
    caption = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', cap_m.group(1))).strip() if cap_m else tid
    t_match = re.search(r'<table[^>]*>(.*?)</table>', content, re.DOTALL)
    if t_match:
        t_rows = parse_html_table(t_match.group(1))
        all_parsed_tables[tid] = {
            "caption": caption,
            "rows": t_rows
        }
        print(f"=== {tid} === ({len(t_rows)} rows)")
        print("Caption:", caption[:80])
        if t_rows:
            print("Headers:", t_rows[0])
            if len(t_rows) > 1:
                print("First row:", t_rows[1])
        print()

import json
with open("parsed_tables.json", "w", encoding="utf-8") as out_f:
    json.dump(all_parsed_tables, out_f, ensure_ascii=False, indent=2)
print("Saved parsed_tables.json successfully!")
