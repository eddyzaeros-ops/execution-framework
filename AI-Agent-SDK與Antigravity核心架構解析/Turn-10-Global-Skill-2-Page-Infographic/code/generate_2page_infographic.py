import os
from PIL import Image, ImageDraw, ImageFont

def create_4k_infographics():
    src_img_path = r"C:\Users\calsa\.gemini\antigravity\brain\d370b073-cdc2-4743-874a-d235b8d87045\harness_infographic_fig_1791409150804.jpg"
    out_dir = r"d:\JavaDO\執行框架"
    
    # -------------------------------------------------------------
    # 1. FIG.PNG: 4K (3840 x 2160)
    # -------------------------------------------------------------
    img = Image.open(src_img_path)
    fig_4k = img.resize((3840, 2160), Image.Resampling.LANCZOS)
    fig_path = os.path.join(out_dir, "fig.png")
    fig_4k.save(fig_path, "PNG", quality=100)
    print("Saved fig.png 4K successfully:", fig_path)

    # -------------------------------------------------------------
    # 2. DOC.PNG: 4K (3840 x 2160) - ULTRA-CLEAR EXTRA LARGE TYPOGRAPHY
    # -------------------------------------------------------------
    CANVAS_W, CANVAS_H = 3840, 2160
    canvas = Image.new("RGB", (CANVAS_W, CANVAS_H), (255, 255, 255))
    draw = ImageDraw.Draw(canvas)

    font_dir = os.path.join(os.environ.get('WINDIR', 'C:\\Windows'), 'Fonts')
    font_bold_path = os.path.join(font_dir, 'msjhbd.ttc')
    font_reg_path = os.path.join(font_dir, 'msjh.ttc')

    # Header fonts
    font_header_tag = ImageFont.truetype(font_bold_path, 36)
    font_header_title = ImageFont.truetype(font_bold_path, 72)
    font_header_sub = ImageFont.truetype(font_bold_path, 38)

    # Column fonts
    font_col_badge = ImageFont.truetype(font_bold_path, 34)
    font_col_title = ImageFont.truetype(font_bold_path, 54)
    font_col_sub = ImageFont.truetype(font_bold_path, 34)

    # Items fonts (ENLARGED TO 44pt BOLD & 38pt BODY)
    font_item_title = ImageFont.truetype(font_bold_path, 44)
    font_item_body = ImageFont.truetype(font_bold_path, 36)  # Use bold/semi-bold for crisp contrast

    # Color Palette
    C_BG_CARD = (252, 252, 252)
    C_BORDER = (210, 215, 222)
    C_DARK = (18, 24, 34)
    C_TEXT_BODY = (45, 55, 72)
    
    C_DIM1 = (30, 95, 170)    # Cobalt / Slate Blue
    C_DIM2 = (40, 120, 80)    # Emerald / Sage
    C_DIM3 = (185, 75, 25)    # Warm Amber / Terra

    # Draw Header
    draw.rounded_rectangle([100, 75, 720, 140], radius=16, fill=(238, 243, 250), outline=C_BORDER, width=2)
    draw.text((130, 88), "✦ arXiv:2609.00006v1 深度研析資訊圖表", font=font_header_tag, fill=C_DIM1)

    draw.text((100, 160), "Harness Engineering: 編程智慧體架構與演化剖析", font=font_header_title, fill=C_DARK)
    draw.text((100, 260), "三大核心維度解構 · 47 項生產級特徵對比 · 破除模型萬能論，確立 AI-ROS 確定性執行基底", font=font_header_sub, fill=(90, 100, 115))

    draw.line([100, 330, CANVAS_W - 100, 330], fill=(220, 225, 232), width=3)

    # 3 Column Dimensions - 4 Focused Points Each with Big Clear Fonts
    columns_data = [
        {
            "num": "DIMENSION 01",
            "title": "運行時核心與驅動",
            "en_title": "Runtime Core & Loops (D1-D2)",
            "color": C_DIM1,
            "items": [
                ("確定性等式：Agent = Model + Harness", "LLM 僅為無狀態機率預測器，複雜軟體交付 90% 失敗源於 Harness 脆弱。Harness 是動態狀態全棧運行時。"),
                ("D1 驅動迴圈：三大主流架構演化", "涵蓋 Iterative 單循環、Aider 語法/測試錯誤反思雙循環 (Reflection)，與 Claude/Codex 工兵派工模式。"),
                ("D2 模型整合：Prompt 快取邊界", "單原廠深度調校超越多模型抽象。嚴格維護 Prefill 快取前綴，落實反鍍金規則 (Anti-gold-plating)。"),
                ("死循環與失控熔斷 (Stuck Detectors)", "生產級 Harness 內建重複動作哈希比對、死循環偵測器、Token 預算硬上限與外部中斷監聽機制。")
            ]
        },
        {
            "num": "DIMENSION 02",
            "title": "動作工具與記憶上下文",
            "en_title": "Tools, Action & Memory (D3-D4)",
            "color": C_DIM2,
            "items": [
                ("D3 工具系統：精簡高確定性", "收斂至 4~8 個原生原子工具（Bash、Read、Write、Search）。全面放棄整檔重寫，採 Search-Replace 區塊替換。"),
                ("寬容瀑布機制 (Fuzzy 95%)", "行號位移自動校正、空白正規化與多行模糊容錯，使代碼編輯成功率自 60% 躍升至 92% 以上。"),
                ("D4 記憶壓縮：閾值邊界淘汰", "捨棄盲目線性追加。距離上限 13K Buffer 觸發壓縮，剝離冗長輸出並保留最近 30% 推理尾端。"),
                ("兩大震撼缺席：零向量代碼 RAG", "生產級 Harness 100% 拋棄向量代碼檢索，由 ripgrep / AST 語法樹完全取代；零採用 LangChain 通用框架。")
            ]
        },
        {
            "num": "DIMENSION 03",
            "title": "安全防禦、多代理與擴展",
            "en_title": "Governance, Scale & Extensibility (D5-D7)",
            "color": C_DIM3,
            "items": [
                ("D5 安全體系：多層防護與沙盒", "Starlark 策略腳本、Bubblewrap/Docker 容器隔離、外部 Guardian 審查模型與人機協同審批 (HITL)。"),
                ("D6 多代理拓撲：拒絕聊天室廣播", "由單代理向層次線程樹 (Codex) 與遞迴派工 (Claude) 演化，跨分支共享只讀快取並支援原子回滾。"),
                ("D7 擴展雙標準：SKILL.md 與 MCP", "SKILL.md (9/11) 以階層 Markdown 定義領域知識；MCP 協議 (8/11) 統一外部工具，延遲加載省 90% 提示空間。"),
                ("大一統趨勢：CLI 演化為平台作業系統", "以 Agentic AI-ROS 為核心，會話基底、全流程審計與動態擴展推動 Coding Harness 轉化為自主軟體工程基礎設施。")
            ]
        }
    ]

    card_y = 370
    card_h = 1710
    card_w = 1160
    gap = 80
    start_x = 100

    for i, col in enumerate(columns_data):
        cx = start_x + i * (card_w + gap)
        accent = col["color"]

        # Card Background & Outer Border
        draw.rounded_rectangle([cx, card_y, cx + card_w, card_y + card_h], radius=26, fill=C_BG_CARD, outline=C_BORDER, width=3)

        # Top Accent Color Bar
        draw.rounded_rectangle([cx + 3, card_y + 3, cx + card_w - 3, card_y + 22], radius=10, fill=accent)

        # Column Header Badge
        badge_w, badge_h = 260, 56
        draw.rounded_rectangle([cx + 50, card_y + 45, cx + 50 + badge_w, card_y + 45 + badge_h], radius=14, fill=accent)
        draw.text((cx + 72, card_y + 54), col["num"], font=font_col_badge, fill=(255, 255, 255))

        # Column Titles
        draw.text((cx + 50, card_y + 125), col["title"], font=font_col_title, fill=C_DARK)
        draw.text((cx + 50, card_y + 205), col["en_title"], font=font_col_sub, fill=accent)

        # Divider
        draw.line([cx + 50, card_y + 265, cx + card_w - 50, card_y + 265], fill=(215, 222, 230), width=2)

        # Render Items with large clear font
        item_start_y = card_y + 295
        slot_height = 345

        for j, (it_title, it_desc) in enumerate(col["items"]):
            iy = item_start_y + j * slot_height

            # Bullet indicator (Circle)
            draw.ellipse([cx + 50, iy + 10, cx + 80, iy + 40], fill=accent)

            # Item Title
            draw.text((cx + 100, iy), it_title, font=font_item_title, fill=C_DARK)

            # Text wrapping - 22 chars per line for big font
            chars = list(it_desc)
            lines = []
            cur_line = ""
            for ch in chars:
                if len(cur_line) >= 22:
                    lines.append(cur_line)
                    cur_line = ch
                else:
                    cur_line += ch
            if cur_line:
                lines.append(cur_line)

            for l_idx, line_text in enumerate(lines[:4]):
                draw.text((cx + 100, iy + 68 + l_idx * 52), line_text, font=font_item_body, fill=C_TEXT_BODY)

    doc_path = os.path.join(out_dir, "doc.png")
    canvas.save(doc_path, "PNG", quality=100)
    print("Saved doc.png 4K with enlarged typography:", doc_path)

if __name__ == '__main__':
    create_4k_infographics()
