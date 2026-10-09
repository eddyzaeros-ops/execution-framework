import os
import re
import subprocess

with open("paper_raw.html", "r", encoding="utf-8") as f:
    html = f.read()

# Target figures to extract: S2.F1 (Fig 1), S6.F2 (Fig 2), S11.F6 (Fig 6)
target_figs = {
    "S2.F1": "figure_1_original",
    "S6.F2": "figure_2_original",
    "S11.F6": "figure_6_original"
}

edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

for fid, fname in target_figs.items():
    # find figure block
    m = re.search(rf'<figure[^>]*id=["\']{fid}["\'][^>]*>(.*?)</figure>', html, re.DOTALL)
    if not m:
        print(f"Figure {fid} not found!")
        continue
    fig_content = m.group(1)
    
    # create standalone html
    standalone_html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
body {{
    margin: 0;
    padding: 20px;
    background: #ffffff;
    display: inline-block;
}}
svg {{
    display: block;
}}
</style>
</head>
<body>
{fig_content}
</body>
</html>
"""
    html_file = os.path.abspath(f"{fname}.html")
    png_file = os.path.abspath(f"{fname}.png")
    
    with open(html_file, "w", encoding="utf-8") as out_f:
        out_f.write(standalone_html)
        
    cmd = [
        edge_path,
        "--headless",
        "--disable-gpu",
        f"--screenshot={png_file}",
        "--window-size=1200,800",
        "--default-background-color=00000000",
        html_file
    ]
    subprocess.run(cmd, check=True)
    print(f"Generated screenshot: {png_file} (exists: {os.path.exists(png_file)})")
