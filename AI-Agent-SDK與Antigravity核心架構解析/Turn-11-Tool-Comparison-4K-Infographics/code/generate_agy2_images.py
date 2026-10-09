import os
from PIL import Image, ImageDraw, ImageFont

# ==========================================
# 1. 產生滿版 16:9 4K 的 fig_agy2.png
# ==========================================
source_img_path = r"C:\Users\calsa\.gemini\antigravity\brain\5910fbe4-a980-4dd5-a1bc-ec71de838632\agy2_comparison_fig_1791209696389.jpg"
fig_output_path = r"d:\JavaDO\執行框架\fig_agy2.png"
doc_output_path = r"d:\JavaDO\執行框架\doc_agy2.png"

CANVAS_W = 3840
CANVAS_H = 2160

print("Generating full 16:9 4K fig_agy2.png...")
orig_img = Image.open(source_img_path)
fig_img = orig_img.resize((CANVAS_W, CANVAS_H), Image.Resampling.LANCZOS)
fig_img.save(fig_output_path, "PNG", quality=100)
print(f"Saved full-canvas fig_agy2.png: {fig_img.size}")

# ==========================================
# 2. 產生滿版 16:9 4K 大字體中文說明面板 doc_agy2.png
# ==========================================
print("Generating full 16:9 4K doc_agy2.png with large fonts...")
doc_canvas = Image.new("RGB", (CANVAS_W, CANVAS_H), (255, 255, 255))
draw = ImageDraw.Draw(doc_canvas)

font_dir = os.path.join(os.environ.get('WINDIR', 'C:\\Windows'), 'Fonts')
font_bold_path = os.path.join(font_dir, 'msjhbd.ttc')
font_reg_path = os.path.join(font_dir, 'msjh.ttc')

header_tag_font = ImageFont.truetype(font_bold_path, 42)
header_title_font = ImageFont.truetype(font_bold_path, 72)
badge_font = ImageFont.truetype(font_bold_path, 34)
col_title_font = ImageFont.truetype(font_bold_path, 54)
col_sub_font = ImageFont.truetype(font_bold_path, 36)
item_title_font = ImageFont.truetype(font_bold_path, 42)
item_desc_font = ImageFont.truetype(font_reg_path, 36)

top_margin = 100
left_margin = 120
right_margin = CANVAS_W - left_margin

# 頂部標籤
tag_w = 460
tag_h = 75
draw.rounded_rectangle([(left_margin, top_margin), (left_margin + tag_w, top_margin + tag_h)], radius=14, fill=(240, 244, 255))
draw.text((left_margin + 35, top_margin + 12), "工具與引擎對比全覽", fill=(37, 99, 235), font=header_tag_font)

# 大標題
draw.text((left_margin + tag_w + 40, top_margin - 3), "VS Code、Antigravity IDE 與 Antigravity 2.0 核心維度解析", fill=(17, 24, 39), font=header_title_font)

# 頂部分割線
line_y = top_margin + tag_h + 50
draw.line([(left_margin, line_y), (right_margin, line_y)], fill=(229, 231, 235), width=4)

# 三大欄位卡片
card_top_y = line_y + 60
card_bottom_y = CANVAS_H - 120
total_avail_w = right_margin - left_margin
col_gap = 70
col_w = (total_avail_w - col_gap * 2) // 3

columns_data = [
    {
        "badge": "DIMENSION 01",
        "badge_bg": (238, 242, 255),
        "badge_fg": (79, 70, 229),
        "title": "VS Code (傳統開發環境)",
        "sub": "TRADITIONAL CODE EDITOR",
        "items": [
            ("本質與定位 (Editor Substrate)", "經典開源程式碼編輯器，本質是提供人類工程師親手打字、編程的打字機工具。"),
            ("AI 角色 (Passive Copilot)", "AI 僅作為側邊欄聊天視窗或單行代碼補全外掛，無法直接深度操作環境。"),
            ("被動語言伺服器 (Passive LSP)", "僅提供靜態語法高亮、錯誤提示與跳轉定義，缺少動態全專案因果推導大腦。"),
            ("全手動維運負擔 (Manual Execution)", "從建置環境、敲終端指令、看報錯到修復 Bug，100% 仰賴人類手動親力親為。")
        ]
    },
    {
        "badge": "DIMENSION 02",
        "badge_bg": (240, 253, 244),
        "badge_fg": (22, 163, 74),
        "title": "Antigravity IDE (AI 原生桌面)",
        "sub": "AI-NATIVE WORKSPACE",
        "items": [
            ("人機協同工作區 (Pair Space)", "專為人類與 AI 深度協同打造的現代整合環境，非傳統外掛硬塞的次要面板。"),
            ("動態資產預覽 (Artifacts & Canvas)", "原生渲染網頁 UI、Mermaid 架構圖、動態進度與 Markdown 報表，交付透明可見。"),
            ("視覺化 Diff 審查 (Visual Inspection)", "直觀並排對比 Agent 對全專案代碼的修改，點擊即可一鍵審查、合併或還原。"),
            ("背景行程即時監控 (Daemon Tasks)", "深度整合 Terminal，支援長效伺服器、背景編譯任務的即時狀態監聽與日誌串流。")
        ]
    },
    {
        "badge": "DIMENSION 03",
        "badge_bg": (254, 242, 242),
        "badge_fg": (225, 29, 72),
        "title": "Antigravity 2.0 (自主代理大腦)",
        "sub": "AGENTIC ENGINE & BRAIN",
        "items": [
            ("自主工程大腦 (Autonomous Brain)", "Google DeepMind 開發的超級自主 Agent 核心，扮演全端工程師兼架構師角色。"),
            ("多子代理編排 (Subagents Cluster)", "動態派發任務給專屬 Subagent（研究員、除錯專家、排程器），實現高並發協同。"),
            ("全自主終端操作 (Autonomous Shell)", "具備本機 Terminal 與檔案讀寫權限，自動安裝套件、建檔、啟動測試與除錯。"),
            ("自我反思除錯 (Self-Debugging Loop)", "即時感知執行報錯，自主定位錯誤根因、修改程式碼並重新驗證，直到目標達成。")
        ]
    }
]

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
    
    # 欄位標題
    draw.text((x + 50, card_top_y + 130), col["title"], fill=(17, 24, 39), font=col_title_font)
    draw.text((x + 50, card_top_y + 205), col["sub"], fill=(107, 114, 128), font=col_sub_font)
    
    # 分割線
    divider_y = card_top_y + 265
    draw.line([(x + 50, divider_y), (x + col_w - 50, divider_y)], fill=(229, 231, 235), width=2)
    
    curr_y = divider_y + 45
    item_max_w = col_w - 140
    
    for heading, desc in col["items"]:
        draw.ellipse([(x + 52, curr_y + 14), (x + 70, curr_y + 32)], fill=col["badge_fg"])
        draw.text((x + 85, curr_y + 3), heading, fill=(17, 24, 39), font=item_title_font)
        curr_y += 62
        
        desc_lines = wrap_text(desc, item_desc_font, item_max_w)
        for line in desc_lines:
            draw.text((x + 85, curr_y), line, fill=(75, 85, 99), font=item_desc_font)
            curr_y += 54
        
        curr_y += 50

doc_canvas.save(doc_output_path, "PNG", quality=100)
print(f"Saved full-canvas doc_agy2.png: {doc_canvas.size}")
