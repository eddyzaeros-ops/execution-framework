import urllib.request
import re
import os

url = "https://arxiv.org/html/2609.00006v1"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
try:
    with urllib.request.urlopen(req) as resp:
        html = resp.read().decode("utf-8", errors="ignore")
    print("Fetched HTML, length:", len(html))
    
    # Save raw html for analysis
    with open("paper_raw.html", "w", encoding="utf-8") as f:
        f.write(html)
        
    imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', html)
    print("Found images count:", len(imgs))
    for src in imgs:
        print("  Img src:", src)
        
    # Also find figure tags
    figs = re.findall(r'<figure[^>]*>(.*?)</figure>', html, re.DOTALL)
    print("Found <figure> tags count:", len(figs))
    for i, fig in enumerate(figs[:10]):
        print(f"--- Figure tag {i+1} ---")
        print(fig[:400])
except Exception as e:
    print("Error:", e)
