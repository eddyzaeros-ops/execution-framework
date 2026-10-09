import os
from PIL import Image, ImageDraw, ImageFont

# Source image generated earlier
source_img_path = r"C:\Users\calsa\.gemini\antigravity\brain\5910fbe4-a980-4dd5-a1bc-ec71de838632\agent_ecosystem_infographic_1791207622556.jpg"
target_output_path = r"d:\JavaDO\執行框架\AI_Agent_Ecosystem_Architecture_4K.png"

# Target 4K 16:9 canvas dimensions
CANVAS_W = 3840
CANVAS_H = 2160

# Layout split
# Upper diagram height: 1420 px
# Lower explanation panel: 740 px
DIAGRAM_H = 1420
PANEL_H = CANVAS_H - DIAGRAM_H

print("Opening base image...")
base_img = Image.open(source_img_path)

# Resize top infographic to fit exactly CANVAS_W x DIAGRAM_H with high quality Lanczos
diagram_resized = base_img.resize((CANVAS_W, DIAGRAM_H), Image.Resampling.LANCZOS)

# Create 4K canvas (Pure White)
canvas = Image.new("RGB", (CANVAS_W, CANVAS_H), (255, 255, 255))
canvas.paste(diagram_resized, (0, 0))

draw = ImageDraw.Draw(canvas)

# Fonts: Microsoft JhengHei Bold & Regular
font_dir = os.path.join(os.environ['WINDIR'], 'Fonts')
font_bold_path = os.path.join(font_dir, 'msjhbd.ttc')
font_reg_path = os.path.join(font_dir, 'msjh.ttc')

title_font = ImageFont.truetype(font_bold_path, 42)
col_title_font = ImageFont.truetype(font_bold_path, 34)
col_sub_font = ImageFont.truetype(font_bold_path, 26)
body_font = ImageFont.truetype(font_reg_path, 25)
badge_font = ImageFont.truetype(font_bold_path, 22)

# Divider line between diagram and panel
draw.line([(80, DIAGRAM_H + 5), (CANVAS_W - 80, DIAGRAM_H + 5)], fill=(225, 230, 238), width=3)

# Panel Header
header_y = DIAGRAM_H + 35
# Small category tag
draw.rounded_rectangle([(100, header_y), (360, header_y + 44)], radius=8, fill=(240, 244, 250))
draw.text((120, header_y + 8), "架構解析與分工指南", fill=(30, 80, 160), font=badge_font)

draw.text((380, header_y - 2), "AI Agent 核心層級與協同架構解析 (Architecture Breakdown)", fill=(20, 25, 35), font=title_font)

# Three Columns Setup
col_w = (CANVAS_W - 200 - 120) // 3  # ~1146 px per column
col_gap = 60
col_start_x = 100
col_top_y = header_y + 75
card_h = 550

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

for i, col in enumerate(columns_data):
    x = col_start_x + i * (col_w + col_gap)
    # Background card
    draw.rounded_rectangle([(x, col_top_y), (x + col_w, col_top_y + card_h)], radius=16, fill=(249, 250, 252), outline=(228, 233, 240), width=2)
    
    # Card Header
    # Badge
    badge_w = 170
    badge_h = 34
    draw.rounded_rectangle([(x + 30, col_top_y + 25), (x + 30 + badge_w, col_top_y + 25 + badge_h)], radius=6, fill=col["badge_bg"])
    draw.text((x + 42, col_top_y + 29), col["badge"], fill=col["badge_fg"], font=badge_font)
    
    # Title
    draw.text((x + 30, col_top_y + 68), col["title"], fill=(20, 25, 35), font=col_title_font)
    draw.text((x + 30, col_top_y + 112), col["sub"], fill=(120, 130, 145), font=col_sub_font)
    
    # Divider inside card
    draw.line([(x + 30, col_top_y + 148), (x + col_w - 30, col_top_y + 148)], fill=(230, 235, 242), width=2)
    
    # Items
    item_y = col_top_y + 165
    for heading, desc in col["items"]:
        # Bullet indicator
        draw.ellipse([(x + 32, item_y + 9), (x + 42, item_y + 19)], fill=col["badge_fg"])
        # Heading
        draw.text((x + 52, item_y + 3), heading, fill=(25, 30, 45), font=ImageFont.truetype(font_bold_path, 25))
        # Description
        draw.text((x + 52, item_y + 36), desc, fill=(90, 100, 115), font=body_font)
        item_y += 88

# Save final 4K image
canvas.save(target_output_path, "PNG", quality=100)
print(f"Successfully generated 4K infographic with integrated Chinese explanation: {target_output_path}")
