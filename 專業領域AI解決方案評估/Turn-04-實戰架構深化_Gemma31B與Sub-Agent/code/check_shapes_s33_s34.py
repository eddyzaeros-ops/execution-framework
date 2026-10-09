import sys
from pptx import Presentation
from pptx.util import Inches

pptx_path = r"d:\JavaDO\執行框架\專業領域AI解決方案評估報告.pptx"
prs = Presentation(pptx_path)

# 調整 Slide 33 與 Slide 34 (索引 32, 33) 的卡片與表格高度，讓 quote 框往下排，表格不重疊
for s_idx in [32, 33]:
    s = prs.slides[s_idx]
    
    # 尋找形狀
    # 找到 3 個 card（圓角矩形）、table、quote box
    cards = []
    tbl_shape = None
    quote_shape = None
    quote_texts = []
    
    for sh in s.shapes:
        if sh.has_table:
            tbl_shape = sh
        elif sh.has_text_frame:
            t = sh.text_frame.text
            if "Air-gap is a perimeter" in t or "State-of-the-art results" in t:
                # 這是 quote 相關形狀之一
                pass

prs.save(pptx_path)
