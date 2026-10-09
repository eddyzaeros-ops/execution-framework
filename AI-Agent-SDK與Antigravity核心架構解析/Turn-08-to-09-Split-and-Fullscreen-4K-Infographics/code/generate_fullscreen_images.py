import os
from PIL import Image, ImageDraw, ImageFont

# ==========================================
# 1. 產生滿版 16:9 4K 的 fig.png
# ==========================================
source_img_path = r"C:\Users\calsa\.gemini\antigravity\brain\5910fbe4-a980-4dd5-a1bc-ec71de838632\agent_ecosystem_infographic_1791207622556.jpg"
fig_output_path = r"d:\JavaDO\執行框架\fig.png"
doc_output_path = r"d:\JavaDO\執行框架\doc.png"

CANVAS_W = 3840
CANVAS_H = 2160

print("Generating full 16:9 4K fig.png...")
orig_img = Image.open(source_img_path)
# 原始圖比例為 1376:768 = 1.7916... 近似 16:9 (1.777...)
# 直接等比例高畫質 Lanczos 縮放為 3840x2160
fig_img = orig_img.resize((CANVAS_W, CANVAS_H), Image.Resampling.LANCZOS)
fig_img.save(fig_output_path, "PNG", quality=100)
print(f"Saved full-canvas fig.png: {fig_img.size}")

# ==========================================
# 2. 重新排版並產生滿版大字體 16:9 4K 的 doc.png
# ==========================================
print("Generating full 16:9 4K doc.png with large fonts...")
doc_canvas = Image.new("RGB", (CANVAS_W, CANVAS_H), (255, 255, 255))
draw = ImageDraw.Draw(doc_canvas)

font_dir = os.path.join(os.environ['WINDIR'], 'Fonts')
font_bold_path = os.path.join(font_dir, 'msjhbd.ttc')
font_reg_path = os.path.join(font_dir, 'msjh.ttc')

# 放大字體設定（適應 4K 滿版）
header_tag_font = ImageFont.truetype(font_bold_path, 42)
header_title_font = ImageFont.truetype(font_bold_path, 72)
badge_font = ImageFont.truetype(font_bold_path, 34)
col_title_font = ImageFont.truetype(font_bold_path, 54)
col_sub_font = ImageFont.truetype(font_bold_path, 36)
item_title_font = ImageFont.truetype(font_bold_path, 42)
item_desc_font = ImageFont.truetype(font_reg_path, 36)

# 頂部 Header
top_margin = 100
left_margin = 120
right_margin = CANVAS_W - left_margin

# 頂部標籤
tag_w = 440
tag_h = 75
draw.rounded_rectangle([(left_margin, top_margin), (left_margin + tag_w, top_margin + tag_h)], radius=14, fill=(240, 244, 255))
draw.text((left_margin + 35, top_margin + 12), "核心架構與分工指南", fill=(37, 99, 235), font=header_tag_font)

# 大標題
draw.text((left_margin + tag_w + 40, top_margin - 3), "AI Agent 核心層級與協同架構深度解析", fill=(17, 24, 39), font=header_title_font)

# 頂部分割線
line_y = top_margin + tag_h + 50
draw.line([(left_margin, line_y), (right_margin, line_y)], fill=(229, 231, 235), width=4)

# 三大欄位卡片設計
card_top_y = line_y + 60
card_bottom_y = CANVAS_H - 120
card_h = card_bottom_y - card_top_y  # 約 1755px
total_avail_w = right_margin - left_margin
col_gap = 70
col_w = (total_avail_w - col_gap * 2) // 3

columns_data = [
    {
        "badge": "DIMENSION 01",
        "badge_bg": (238, 242, 255),
        "badge_fg": (79, 70, 229),
        "title": "大腦核心與編排協議",
        "sub": "THE BRAIN & ORCHESTRATION",
        "items": [
            ("底層智慧體 (Claude / OpenAI / Google)", "提供超大長上下文窗口、多模態感知與極致的推理與決策邏輯。"),
            ("思維迴圈 (Reasoning & Loops)", "超越單輪對話，具備自主目標規劃、反思修訂 (Self-reflection) 與工具調用。"),
            ("Agent SDK 的角色", "標準化 Tool Calling 與通訊協議，把底層大腦與企業 API/外部工具串接起來。"),
            ("子代理委派 (Subagent Delegation)", "將複雜大任務拆解，動態指派給專用子代理（如對帳、檢索、客訴）並行處理。")
        ]
    },
    {
        "badge": "DIMENSION 02",
        "badge_bg": (240, 253, 244),
        "badge_fg": (22, 163, 74),
        "title": "協同實體與代理引擎",
        "sub": "COLLABORATION & ENGINE",
        "items": [
            ("代表實體 (Antigravity 2.0 / Claude Code)", "軟體工程領域的高級「AI 協同同事」，擁有系統級自主操作權限。"),
            ("代理工作流 (Agentic Workflows)", "自主讀寫整個專案目錄、跨檔案語法分析，主動維護專案架構。"),
            ("終端自主執行 (Terminal Execution)", "能直接在本地終端機執行編譯、安裝依賴套件與測試，無需人工介入。"),
            ("日誌感知與自我修復 (Auto-Debugging)", "即時監聽終端機運行報錯，自動定位錯誤代碼、分析成因並立即修正。")
        ]
    },
    {
        "badge": "DIMENSION 03",
        "badge_bg": (254, 242, 242),
        "badge_fg": (225, 29, 72),
        "title": "開發工作區與終端交付",
        "sub": "WORKSPACE & INTERFACE",
        "items": [
            ("VS Code vs. Antigravity IDE", "VS Code 是手動編寫編輯器；Antigravity IDE 則是專為人機深度協同打造。"),
            ("原生物件與視覺化 (Artifacts & Canvas)", "支援程式碼 Diff 對比、結構圖即時渲染與動態儀表板，提升交付透明度。"),
            ("代碼製造者 vs. 生產成品", "Antigravity 是「製造工程師」，用 Agent SDK 寫出業務代碼交給生產環境。"),
            ("生產環境部署 (Production Deployment)", "將生成的對帳/客服 Agent 封裝上雲（Docker / API），實現 24/7 自動運轉。")
        ]
    }
]

# 輔助函式：自動換行
def wrap_text(text, font, max_width):
    lines = []
    current_line = ""
    for char in text:
        test_line = current_line + char
        bbox = draw.textbbox((0, 0), test_line, font=font)
        if (bbox[2] - bbox[0]) <= max_width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = char
    if current_line:
        lines.append(current_line)
    return lines

for i, col in enumerate(columns_data):
    x = left_margin + i * (col_w + col_gap)
    
    # 卡片外框與背景
    draw.rounded_rectangle([(x, card_top_y), (x + col_w, card_bottom_y)], radius=24, fill=(250, 252, 255), outline=(226, 232, 240), width=3)
    
    # 頂部裝飾色條
    draw.rounded_rectangle([(x, card_top_y), (x + col_w, card_top_y + 14)], radius=8, fill=col["badge_fg"])
    
    # Badge 標籤
    badge_w = 260
    badge_h = 56
    draw.rounded_rectangle([(x + 50, card_top_y + 50), (x + 50 + badge_w, card_top_y + 50 + badge_h)], radius=10, fill=col["badge_bg"])
    draw.text((x + 70, card_top_y + 56), col["badge"], fill=col["badge_fg"], font=badge_font)
    
    # 欄位主標題與副標題
    draw.text((x + 50, card_top_y + 130), col["title"], fill=(17, 24, 39), font=col_title_font)
    draw.text((x + 50, card_top_y + 205), col["sub"], fill=(107, 114, 128), font=col_sub_font)
    
    # 卡片內部裝飾線
    divider_y = card_top_y + 265
    draw.line([(x + 50, divider_y), (x + col_w - 50, divider_y)], fill=(229, 231, 235), width=2)
    
    # 渲染各項目
    curr_y = divider_y + 45
    item_max_w = col_w - 140
    
    for heading, desc in col["items"]:
        # 圓形項目點
        draw.ellipse([(x + 52, curr_y + 14), (x + 70, curr_y + 32)], fill=col["badge_fg"])
        # 標題
        draw.text((x + 85, curr_y + 3), heading, fill=(17, 24, 39), font=item_title_font)
        curr_y += 62
        
        # 內文（自動折行）
        desc_lines = wrap_text(desc, item_desc_font, item_max_w)
        for line in desc_lines:
            draw.text((x + 85, curr_y), line, fill=(75, 85, 99), font=item_desc_font)
            curr_y += 54
        
        curr_y += 50  # 項目間距

doc_canvas.save(doc_output_path, "PNG", quality=100)
print(f"Saved full-canvas doc.png: {doc_canvas.size}")
