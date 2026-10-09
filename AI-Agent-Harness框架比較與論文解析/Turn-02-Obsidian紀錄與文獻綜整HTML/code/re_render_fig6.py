import re
import os
import subprocess

with open("paper_raw.html", "r", encoding="utf-8") as f:
    html = f.read()

m = re.search(r'<figure[^>]*id=["\']S11.F6["\'][^>]*>(.*?)</figure>', html, re.DOTALL)
fig_content = m.group(1)

standalone_html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
body {{
    margin: 0;
    padding: 30px;
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
html_file = os.path.abspath("figure_6_original.html")
png_file = os.path.abspath("figure_6_original.png")

with open(html_file, "w", encoding="utf-8") as out_f:
    out_f.write(standalone_html)
    
edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
cmd = [
    edge_path,
    "--headless",
    "--disable-gpu",
    f"--screenshot={png_file}",
    "--window-size=1400,1200",
    "--default-background-color=00000000",
    html_file
]
subprocess.run(cmd, check=True)

# Crop
from PIL import Image
import numpy as np
img = Image.open(png_file).convert('RGBA')
arr = np.array(img)
mask = (arr[:, :, 0] < 250) | (arr[:, :, 1] < 250) | (arr[:, :, 2] < 250)
coords = np.argwhere(mask)
if len(coords) > 0:
    y0, x0 = coords.min(axis=0)
    y1, x1 = coords.max(axis=0) + 1
    pad = 25
    x0 = max(0, x0 - pad)
    y0 = max(0, y0 - pad)
    x1 = min(img.width, x1 + pad)
    y1 = min(img.height, y1 + pad)
    cropped = img.crop((x0, y0, x1, y1))
    cropped.save("figure_6_original_cropped.png")
    print(f"Saved cropped figure_6_original_cropped.png: size={cropped.size}")
