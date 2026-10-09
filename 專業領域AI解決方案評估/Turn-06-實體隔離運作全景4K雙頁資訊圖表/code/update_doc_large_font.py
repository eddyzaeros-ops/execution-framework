import os
from PIL import Image, ImageDraw, ImageFont

target_dir = r"d:\JavaDO\執行框架"
doc_path = os.path.join(target_dir, "doc.png")

CANVAS_W, CANVAS_H = 3840, 2160
canvas = Image.new("RGB", (CANVAS_W, CANVAS_H), (255, 255, 255))
draw = ImageDraw.Draw(canvas)

# 字型設定
font_dir = os.path.join(os.environ.get('WINDIR', 'C:\\Windows'), 'Fonts')
font_bold = os.path.join(font_dir, 'msjhbd.ttc')
font_reg = os.path.join(font_dir, 'msjh.ttc')

header_badge_font = ImageFont.truetype(font_bold, 36)
header_title_font = ImageFont.truetype(font_bold, 74)
header_sub_font = ImageFont.truetype(font_reg, 38)

card_dim_font = ImageFont.truetype(font_bold, 32)
card_title_font = ImageFont.truetype(font_bold, 54)
card_sub_font = ImageFont.truetype(font_bold, 34)

# 【核心字級加大】：標題 48pt、內文 40pt、序號 40pt
item_num_font = ImageFont.truetype(font_bold, 40)
item_title_font = ImageFont.truetype(font_bold, 48)
item_desc_font = ImageFont.truetype(font_reg, 40)

# 顏色定義
COLOR_BG = (255, 255, 255)
COLOR_CARD_BG = (250, 249, 246)
COLOR_CARD_BORDER = (230, 226, 218)
COLOR_TEXT_MAIN = (44, 62, 80)
COLOR_TEXT_MUTED = (108, 122, 137)
COLOR_TEXT_BODY = (50, 60, 75)

THEME_SAGE = (74, 107, 93)     # #4A6B5D
THEME_TERRA = (200, 106, 75)   # #C86A4B
THEME_SLATE = (71, 85, 105)    # #475569

# 頂部膠囊 Badge
draw.rounded_rectangle([120, 80, 480, 140], radius=30, fill=(232, 226, 213))
draw.text((150, 92), "實體隔離專屬架構說明", font=header_badge_font, fill=COLOR_TEXT_MAIN)

# 主標題與副標題
draw.text((120, 160), "實體隔離環境的 AI Agent 運作全景深度解析", font=header_title_font, fill=COLOR_TEXT_MAIN)
draw.text((120, 248), "零外網連線、單卡高承載、代碼沙箱與 AST 雙重隔離：在絕對安全受控下釋放國防科研生產力", font=header_sub_font, fill=COLOR_TEXT_MUTED)

# 頂部細分割線
draw.line([(120, 310), (3720, 310)], fill=(220, 215, 205), width=3)

# 3 欄卡片佈局
COL_W = 1146
COL_GAP = 80
CARD_TOP = 345
CARD_H = 1715

# 精煉強化的 1, 2, 3, 4 核心要點（去冗字、聚焦要害，確保 40pt 大字體下完美舒展）
COLUMNS_DATA = [
    {
        "dim": "DIMENSION 01",
        "title": "物理隔離與資料入庫",
        "subtitle": "Physical Isolation & Ingestion",
        "color": THEME_SAGE,
        "items": [
            ("實體單向隔離光閘 (Data Diode)", "外部標準件手冊、公開文獻與依賴庫，僅能透過單向光閘或唯讀光碟單向導入，徹底阻斷外洩通道。"),
            ("入庫合規與靜態消殺驗證", "入網前全面執行多重防毒引擎消殺與敏感審計，嚴防惡意 Payload 暗中混入離線訓練集或 RAG 文件。"),
            ("離線離子化知識庫 (Offline Docs)", "構建結構化軍規標準手冊（MIL-STD）與歷年科研測試報告，以純文字 Markdown 沉澱，零外部依賴。"),
            ("嚴格授權與身分硬體鎖", "研發工程師存取內網核心運算資源均採多因素硬體憑證（Smart Card / FIDO2），從源頭控制操作邊界。")
        ]
    },
    {
        "dim": "DIMENSION 02",
        "title": "地端核心智慧與調度",
        "subtitle": "On-Prem Core Intelligence",
        "color": THEME_TERRA,
        "items": [
            ("Google Gemma 31B 稠密模型", "評估兼顧單卡推論效率與深度推理的最佳模型；單張 A100 / RTX 4090 (Q4) 即可流暢落地，免多卡巨額成本。"),
            ("雙軌專業 Harness 框架", "整合 OpenCode（代碼語法與上下文約束）與 Hermes Agent（工具決策循環），精準執行多步驟科研排錯。"),
            ("LangChain DeepAgents 多層調度", "以 Supervisor-Worker 模式協同多個專職 Sub-Agent，將複雜任務分解為高可控、可驗證的狀態機步驟。"),
            ("Git-Backed 本地第二大腦", "任務決策鏈、反思與踩坑教訓即時 commit 至私有 Git Repo 與 Obsidian Vault，沉澱為組織永久智產。")
        ]
    },
    {
        "dim": "DIMENSION 03",
        "title": "國防級沙箱執行與審計",
        "subtitle": "Defense-Grade Sandboxed Execution",
        "color": THEME_SLATE,
        "items": [
            ("確定性密封沙箱 (Deterministic Sandbox)", "Agent 執行的 Python/C++ 腳本與工程計算，均在徹底斷網且限制資源的 Docker / gVisor 沙箱內運行。"),
            ("AST 語法樹靜態安全閘 (Security Gate)", "代碼執行前由 Pre-Tool Hook 解析 AST 樹，嚴格攔截危險系統呼叫（如 socket, subprocess, rm -rf）。"),
            ("仿真 API 受控適配器 (Simulation API)", "僅開放特定且經白名單驗證的本機 CAE 求解器（結構、熱力、流體網格），嚴禁任何武器殺傷鏈接駁。"),
            ("不可篡改之唯讀審計日誌 (Audit Log)", "所有 Prompt、推論鏈、工具呼叫參數均賦予唯一 UUID Trace ID，實時寫入唯讀稽核存儲，符合軍規追溯性。")
        ]
    }
]

def draw_wrapped_text(draw, text, font, fill, x, y, max_w, line_spacing=12):
    cur_y = y
    line = ""
    for char in text:
        test_line = line + char
        bbox = draw.textbbox((x, cur_y), test_line, font=font)
        if bbox[2] - x > max_w:
            draw.text((x, cur_y), line, font=font, fill=fill)
            line = char
            cur_y += (bbox[3] - bbox[1]) + line_spacing
        else:
            line = test_line
    if line:
        draw.text((x, cur_y), line, font=font, fill=fill)
        cur_y += (draw.textbbox((x, cur_y), line, font=font)[3] - cur_y) + line_spacing
    return cur_y

for i, col in enumerate(COLUMNS_DATA):
    x = 120 + i * (COL_W + COL_GAP)
    
    # 卡片外框與背景
    draw.rounded_rectangle([x, CARD_TOP, x + COL_W, CARD_TOP + CARD_H], radius=24, fill=COLOR_CARD_BG, outline=COLOR_CARD_BORDER, width=2)
    
    # 卡片頂部主題色彩標條
    draw.rounded_rectangle([x, CARD_TOP, x + COL_W, CARD_TOP + 16], radius=8, fill=col["color"])
    
    # 頂部 DIMENSION 徽章
    dim_box_w = 260
    draw.rounded_rectangle([x + 45, CARD_TOP + 40, x + 45 + dim_box_w, CARD_TOP + 92], radius=16, fill=col["color"])
    draw.text((x + 65, CARD_TOP + 48), col["dim"], font=card_dim_font, fill=(255, 255, 255))
    
    # 欄位標題與英文副標
    draw.text((x + 45, CARD_TOP + 112), col["title"], font=card_title_font, fill=COLOR_TEXT_MAIN)
    draw.text((x + 45, CARD_TOP + 180), col["subtitle"], font=card_sub_font, fill=COLOR_TEXT_MUTED)
    
    # 卡片內細分隔線
    draw.line([(x + 45, CARD_TOP + 236), (x + COL_W - 45, CARD_TOP + 236)], fill=(225, 220, 210), width=2)
    
    # 渲染 4 個要點
    item_y = CARD_TOP + 265
    for idx, (ititle, idesc) in enumerate(col["items"]):
        # 序號標記圓圈（放大半徑至 28px）
        circle_r = 28
        cx, cy = x + 75, item_y + 30
        draw.ellipse([cx - circle_r, cy - circle_r, cx + circle_r, cy + circle_r], fill=col["color"])
        draw.text((cx - 12, cy - 25), str(idx + 1), font=item_num_font, fill=(255, 255, 255))
        
        # 項目標題（48pt 粗體）
        draw.text((x + 125, item_y), ititle, font=item_title_font, fill=COLOR_TEXT_MAIN)
        
        # 內文段落（40pt 大字體自動換行）
        item_y = draw_wrapped_text(draw, idesc, item_desc_font, COLOR_TEXT_BODY, x + 125, item_y + 68, COL_W - 175, line_spacing=14)
        item_y += 38  # 項目間距

# 底部狀態列標註
draw.line([(120, 2085), (3720, 2085)], fill=(230, 225, 215), width=2)
footer_font = ImageFont.truetype(font_reg, 30)
draw.text((120, 2100), "國防專案領域 AI 落地指南 · 實體隔離架構全景 (AIR-GAPPED OPERATIONAL BLUEPRINT) · 純文字/沙箱/不可篡改審計", font=footer_font, fill=COLOR_TEXT_MUTED)
draw.text((3340, 2100), "PAGE 02 / EXPLANATION", font=footer_font, fill=COLOR_TEXT_MUTED)

canvas.save(doc_path, "PNG", quality=100)
print(f"Successfully generated enlarged doc.png at: {doc_path}")
