"""
Advanced PPTX Generator for arXiv:2609.00006v1 Harness Engineering Study.
Strictly adheres to Template 1 (Warm Editorial Minimalism) with enlarged fonts,
fully redrawn Figure 1 (D1-D7 Architecture), Figure 2, Figure 4, Figure 5, Figure 6, Figure 7,
and comprehensive cross-cutting tables and 18 practical recommendations.
"""

import os
import sys
import pptx
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

# Template 1 Color Specification
BG_CANVAS = RGBColor(0xF5, 0xF2, 0xEB)        # Soft Oat / Warm Linen
BG_CARD = RGBColor(0xFD, 0xFC, 0xFA)          # Warm Cream White
BORDER_CARD = RGBColor(0xE3, 0xDC, 0xCF)      # Subtle Sandline border
BORDER_DIVIDER = RGBColor(0xD6, 0xCE, 0xBF)   # Delicate hairline divider

BRAND_SLATE = RGBColor(0x2C, 0x3E, 0x50)      # Deep Mineral Slate
BRAND_SAGE = RGBColor(0x3B, 0x6E, 0x58)       # Grounded Sage Green
BRAND_TERRA = RGBColor(0x9E, 0x5A, 0x38)      # Warm Terracotta
BRAND_OCHRE = RGBColor(0xB4, 0x78, 0x2A)      # Warm Ochre

TEXT_HEADLINE = RGBColor(0x23, 0x2D, 0x38)    # Charcoal Slate
TEXT_BODY = RGBColor(0x3E, 0x48, 0x56)        # Darkened Warm Slate for high contrast & clarity
TEXT_MUTED = RGBColor(0x65, 0x71, 0x82)       # Soft Slate 600

TABLE_HEADER_BG = RGBColor(0xEA, 0xE4, 0xD8)  # Warm Oat Table Header
TABLE_ROW_ALT = RGBColor(0xF7, 0xF4, 0xED)    # Alternate warm row tint

FONT_HEADING = "Microsoft JhengHei"
FONT_BODY = "Microsoft JhengHei"

TOTAL_SLIDES = 22

def init_presentation():
    prs = pptx.Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    return prs

def apply_warm_background(slide):
    bg_rect = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg_rect.fill.solid()
    bg_rect.fill.fore_color.rgb = BG_CANVAS
    bg_rect.line.fill.background()
    
    top_bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(0.04))
    top_bar.fill.solid()
    top_bar.fill.fore_color.rgb = BRAND_SAGE
    top_bar.line.fill.background()

def add_header(slide, title_text, category_text, subtitle_text=""):
    cat_box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(0.28), Inches(2.5), Inches(0.32))
    cat_box.fill.solid()
    cat_box.fill.fore_color.rgb = RGBColor(0xE8, 0xE2, 0xD5)
    cat_box.line.color.rgb = BORDER_CARD
    cat_box.line.width = Pt(0.75)
    tf_cat = cat_box.text_frame
    tf_cat.margin_left = tf_cat.margin_top = tf_cat.margin_right = tf_cat.margin_bottom = 0
    p_cat = tf_cat.paragraphs[0]
    p_cat.alignment = PP_ALIGN.CENTER
    r_cat = p_cat.add_run()
    r_cat.text = f"✦  {category_text}"
    r_cat.font.name = FONT_HEADING
    r_cat.font.size = Pt(10)
    r_cat.font.bold = True
    r_cat.font.color.rgb = BRAND_SAGE
    
    tb_title = slide.shapes.add_textbox(Inches(0.8), Inches(0.64), Inches(11.733), Inches(0.85))
    tf_title = tb_title.text_frame
    tf_title.word_wrap = True
    tf_title.margin_left = tf_title.margin_top = tf_title.margin_right = tf_title.margin_bottom = 0
    
    p0 = tf_title.paragraphs[0]
    r_title = p0.add_run()
    r_title.text = title_text
    r_title.font.name = FONT_HEADING
    r_title.font.size = Pt(17.5)
    r_title.font.bold = True
    r_title.font.color.rgb = TEXT_HEADLINE
    
    if subtitle_text:
        p1 = tf_title.add_paragraph()
        p1.space_before = Pt(3)
        r_sub = p1.add_run()
        r_sub.text = subtitle_text
        r_sub.font.name = FONT_BODY
        r_sub.font.size = Pt(10)
        r_sub.font.color.rgb = TEXT_MUTED
        
    divider = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.52), Inches(11.733), Inches(0.015))
    divider.fill.solid()
    divider.fill.fore_color.rgb = BORDER_DIVIDER
    divider.line.fill.background()

def add_footer(slide, current_idx, total_slides=TOTAL_SLIDES):
    tb = slide.shapes.add_textbox(Inches(0.8), Inches(7.14), Inches(9.0), Inches(0.25))
    tf = tb.text_frame
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
    p = tf.paragraphs[0]
    r = p.add_run()
    r.text = "AI AGENT HARNESS ENGINEERING  ·  ARCHITECTURAL SPECIFICATION & BENCHMARK (arXiv:2609.00006v1)"
    r.font.name = FONT_BODY
    r.font.size = Pt(8.5)
    r.font.color.rgb = TEXT_MUTED
    
    tb2 = slide.shapes.add_textbox(Inches(11.0), Inches(7.14), Inches(1.533), Inches(0.25))
    tf2 = tb2.text_frame
    tf2.margin_left = tf2.margin_top = tf2.margin_right = tf2.margin_bottom = 0
    p2 = tf2.paragraphs[0]
    p2.alignment = PP_ALIGN.RIGHT
    r2 = p2.add_run()
    r2.text = f"{current_idx:02d} / {total_slides:02d}"
    r2.font.name = FONT_BODY
    r2.font.size = Pt(9)
    r2.font.bold = True
    r2.font.color.rgb = BRAND_SAGE

def add_enlarged_bullet_card(slide, left, top, width, height, title, items, tag=None, accent_color=BRAND_SAGE):
    """
    Template 1 Bullet Card with ENLARGED readable fonts:
    - Title: 12pt Bold
    - Item Header: 10.5pt Bold
    - Item Body: 10pt Regular (high contrast, clearly legible)
    - Solid Circular Badge: 0.28" with pure white centered number
    """
    card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(left), Inches(top), Inches(width), Inches(height))
    card.fill.solid()
    card.fill.fore_color.rgb = BG_CARD
    card.line.color.rgb = BORDER_CARD
    card.line.width = Pt(1)
    
    # Title row
    tb_t = slide.shapes.add_textbox(Inches(left + 0.2), Inches(top + 0.12), Inches(width - 0.4), Inches(0.38))
    tf_t = tb_t.text_frame
    tf_t.word_wrap = True
    tf_t.margin_left = tf_t.margin_top = tf_t.margin_right = tf_t.margin_bottom = 0
    p0 = tf_t.paragraphs[0]
    r0 = p0.add_run()
    r0.text = title
    r0.font.name = FONT_HEADING
    r0.font.size = Pt(12)
    r0.font.bold = True
    r0.font.color.rgb = TEXT_HEADLINE
    
    if tag:
        r_tag = p0.add_run()
        r_tag.text = f"  [{tag}]"
        r_tag.font.name = FONT_BODY
        r_tag.font.size = Pt(9.5)
        r_tag.font.bold = True
        r_tag.font.color.rgb = accent_color
        
    div = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(left + 0.2), Inches(top + 0.52), Inches(width - 0.4), Inches(0.012))
    div.fill.solid()
    div.fill.fore_color.rgb = BORDER_DIVIDER
    div.line.fill.background()
    
    # Calculate item slots
    num_items = len(items)
    content_top = top + 0.60
    available_h = height - 0.70
    slot_h = available_h / num_items
    
    for idx, item in enumerate(items):
        item_y = content_top + idx * slot_h
        
        # Solid circular badge
        circle_dia = 0.26
        badge_c = accent_color if idx % 2 == 0 else BRAND_TERRA
        badge = slide.shapes.add_shape(
            MSO_SHAPE.OVAL,
            Inches(left + 0.2),
            Inches(item_y + 0.04),
            Inches(circle_dia),
            Inches(circle_dia)
        )
        badge.fill.solid()
        badge.fill.fore_color.rgb = badge_c
        badge.line.fill.background()
        tf_b = badge.text_frame
        tf_b.margin_left = tf_b.margin_top = tf_b.margin_right = tf_b.margin_bottom = 0
        p_b = tf_b.paragraphs[0]
        p_b.alignment = PP_ALIGN.CENTER
        r_b = p_b.add_run()
        r_b.text = f"{idx+1}"
        r_b.font.name = FONT_HEADING
        r_b.font.size = Pt(9)
        r_b.font.bold = True
        r_b.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        
        # Text box
        tb_i = slide.shapes.add_textbox(Inches(left + 0.54), Inches(item_y), Inches(width - 0.74), Inches(slot_h - 0.04))
        tf_i = tb_i.text_frame
        tf_i.word_wrap = True
        tf_i.margin_left = tf_i.margin_top = tf_i.margin_right = tf_i.margin_bottom = 0
        p_i = tf_i.paragraphs[0]
        p_i.line_spacing = 1.15
        
        if "：" in item:
            parts = item.split("：", 1)
            rh = p_i.add_run()
            rh.text = parts[0] + "："
            rh.font.name = FONT_HEADING
            rh.font.size = Pt(10.5)
            rh.font.bold = True
            rh.font.color.rgb = BRAND_SLATE
            
            rb = p_i.add_run()
            rb.text = parts[1]
            rb.font.name = FONT_BODY
            rb.font.size = Pt(10)
            rb.font.color.rgb = TEXT_BODY
        else:
            rb = p_i.add_run()
            rb.text = item
            rb.font.name = FONT_BODY
            rb.font.size = Pt(10)
            rb.font.color.rgb = TEXT_BODY

def add_centered_quote_card(slide, left, top, width, height, en_quote, highlight_word, zh_quote):
    card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(left), Inches(top), Inches(width), Inches(height))
    card.fill.solid()
    card.fill.fore_color.rgb = BG_CARD
    card.line.color.rgb = BORDER_CARD
    card.line.width = Pt(1)
    
    tb = slide.shapes.add_textbox(Inches(left + 0.3), Inches(top + 0.15), Inches(width - 0.6), Inches(height - 0.3))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
    
    p0 = tf.paragraphs[0]
    p0.alignment = PP_ALIGN.CENTER
    
    if highlight_word and highlight_word in en_quote:
        before, after = en_quote.split(highlight_word, 1)
        r0 = p0.add_run()
        r0.text = f'"{before}'
        r0.font.name = FONT_HEADING
        r0.font.size = Pt(13)
        r0.font.bold = True
        r0.font.color.rgb = BRAND_SLATE
        
        r_hl = p0.add_run()
        r_hl.text = highlight_word
        r_hl.font.name = FONT_HEADING
        r_hl.font.size = Pt(13)
        r_hl.font.bold = True
        r_hl.font.color.rgb = BRAND_TERRA
        
        r1 = p0.add_run()
        r1.text = f'{after}"'
        r1.font.name = FONT_HEADING
        r1.font.size = Pt(13)
        r1.font.bold = True
        r1.font.color.rgb = BRAND_SLATE
    else:
        r0 = p0.add_run()
        r0.text = f'"{en_quote}"'
        r0.font.name = FONT_HEADING
        r0.font.size = Pt(13)
        r0.font.bold = True
        r0.font.color.rgb = BRAND_SLATE
        
    p1 = tf.add_paragraph()
    p1.space_before = Pt(6)
    p1.alignment = PP_ALIGN.CENTER
    r_zh = p1.add_run()
    r_zh.text = zh_quote
    r_zh.font.name = FONT_BODY
    r_zh.font.size = Pt(10.5)
    r_zh.font.color.rgb = TEXT_MUTED

def create_enlarged_table(slide, left, top, width, height, headers, rows_data, col_widths=None, font_size=9.5):
    """Creates a modern styled table with enlarged fonts (9.5pt~10pt) for high readability."""
    container = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(left), Inches(top), Inches(width), Inches(height))
    container.fill.solid()
    container.fill.fore_color.rgb = BG_CARD
    container.line.color.rgb = BORDER_CARD
    container.line.width = Pt(1)
    
    t_left = left + 0.12
    t_top = top + 0.10
    t_width = width - 0.24
    t_height = height - 0.20
    
    num_rows = len(rows_data) + 1
    num_cols = len(headers)
    table_shape = slide.shapes.add_table(num_rows, num_cols, Inches(t_left), Inches(t_top), Inches(t_width), Inches(t_height))
    table = table_shape.table
    
    if col_widths and len(col_widths) == num_cols:
        scale = t_width / sum(col_widths)
        for idx, w in enumerate(col_widths):
            table.columns[idx].width = Inches(w * scale)
            
    # Headers
    for c_idx, h_text in enumerate(headers):
        cell = table.cell(0, c_idx)
        cell.fill.solid()
        cell.fill.fore_color.rgb = TABLE_HEADER_BG
        cell.vertical_anchor = MSO_ANCHOR.MIDDLE
        p = cell.text_frame.paragraphs[0]
        p.text = h_text
        p.alignment = PP_ALIGN.LEFT if c_idx == 0 else PP_ALIGN.CENTER
        p.font.name = FONT_HEADING
        p.font.size = Pt(font_size + 0.5)
        p.font.bold = True
        p.font.color.rgb = TEXT_HEADLINE
        
    # Data Rows
    for r_idx, r_data in enumerate(rows_data):
        row_bg = TABLE_ROW_ALT if r_idx % 2 == 1 else BG_CARD
        for c_idx, val in enumerate(r_data):
            cell = table.cell(r_idx + 1, c_idx)
            cell.fill.solid()
            cell.fill.fore_color.rgb = row_bg
            cell.vertical_anchor = MSO_ANCHOR.MIDDLE
            p = cell.text_frame.paragraphs[0]
            p.text = str(val)
            p.font.name = FONT_BODY
            p.font.size = Pt(font_size)
            p.alignment = PP_ALIGN.LEFT if c_idx == 0 else (PP_ALIGN.CENTER if len(str(val)) <= 15 else PP_ALIGN.LEFT)
            if c_idx == 0:
                p.font.bold = True
                p.font.color.rgb = TEXT_HEADLINE
            else:
                p.font.color.rgb = TEXT_BODY

# ==============================================================================
# MAIN SLIDE BUILDER FUNCTION
# ==============================================================================
def build_all_slides():
    prs = init_presentation()
    blank_layout = prs.slide_layouts[6]
    
    # --------------------------------------------------------------------------
    # SLIDE 1: 封面 (Title Slide)
    # --------------------------------------------------------------------------
    s1 = prs.slides.add_slide(blank_layout)
    apply_warm_background(s1)
    
    hero = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.2), Inches(11.733), Inches(5.4))
    hero.fill.solid()
    hero.fill.fore_color.rgb = BG_CARD
    hero.line.color.rgb = BORDER_CARD
    hero.line.width = Pt(1)
    
    tag = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.3), Inches(1.65), Inches(3.6), Inches(0.38))
    tag.fill.solid()
    tag.fill.fore_color.rgb = RGBColor(0xEA, 0xE4, 0xD8)
    tag.line.color.rgb = BORDER_CARD
    tag.line.width = Pt(0.75)
    tf_tag = tag.text_frame
    tf_tag.margin_left = tf_tag.margin_top = tf_tag.margin_right = tf_tag.margin_bottom = 0
    p_t = tf_tag.paragraphs[0]
    p_t.alignment = PP_ALIGN.CENTER
    r_t = p_t.add_run()
    r_t.text = "✦  arXiv:2609.00006v1 學術深度重磅解析"
    r_t.font.name = FONT_HEADING
    r_t.font.size = Pt(11)
    r_t.font.bold = True
    r_t.font.color.rgb = BRAND_SAGE
    
    tb1 = s1.shapes.add_textbox(Inches(1.3), Inches(2.25), Inches(10.7), Inches(2.5))
    tf1 = tb1.text_frame
    tf1.word_wrap = True
    tf1.margin_left = tf1.margin_top = tf1.margin_right = tf1.margin_bottom = 0
    
    p = tf1.paragraphs[0]
    r = p.add_run()
    r.text = "Harness Engineering: 編程智慧體架構與演化剖析"
    r.font.name = FONT_HEADING
    r.font.size = Pt(26)
    r.font.bold = True
    r.font.color.rgb = TEXT_HEADLINE
    
    p_sub = tf1.add_paragraph()
    p_sub.space_before = Pt(10)
    r_sub = p_sub.add_run()
    r_sub.text = "Anatomy, Architecture, and Evolution of Coding Agents — A Source-Code Study of Eleven Systems"
    r_sub.font.name = FONT_BODY
    r_sub.font.size = Pt(12)
    r_sub.font.color.rgb = BRAND_TERRA
    
    p_desc = tf1.add_paragraph()
    p_desc.space_before = Pt(12)
    r_desc = p_desc.add_run()
    r_desc.text = "跨 11 款主流生產級系統原始碼深度審查 · 47 項特徵矩陣 · 重繪七大子系統圖標與拓撲 · 18 條架構實踐軍規"
    r_desc.font.name = FONT_BODY
    r_desc.font.size = Pt(11)
    r_desc.font.color.rgb = TEXT_BODY
    
    div_h = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(1.3), Inches(5.1), Inches(10.733), Inches(0.015))
    div_h.fill.solid()
    div_h.fill.fore_color.rgb = BORDER_DIVIDER
    div_h.line.fill.background()
    
    tb_meta = s1.shapes.add_textbox(Inches(1.3), Inches(5.3), Inches(10.7), Inches(0.8))
    tf_meta = tb_meta.text_frame
    tf_meta.word_wrap = True
    tf_meta.margin_left = tf_meta.margin_top = tf_meta.margin_right = tf_meta.margin_bottom = 0
    p_m = tf_meta.paragraphs[0]
    r_m = p_m.add_run()
    r_m.text = "論文作者：Paul Barbaste, Tristan Darrigol, Germain Vu, Tom Wiltberger (Wavestone AI Lab)\n分析維度：D1 驅動迴圈、D2 模型協同、D3 工具系統、D4 記憶管理、D5 安全防禦、D6 代理協同、D7 擴展標準"
    r_m.font.name = FONT_BODY
    r_m.font.size = Pt(10)
    r_m.font.color.rgb = TEXT_MUTED
    
    add_footer(s1, 1)

    # --------------------------------------------------------------------------
    # SLIDE 2: 核心命題與定義澄清 (Core Thesis & Definitions)
    # --------------------------------------------------------------------------
    s2 = prs.slides.add_slide(blank_layout)
    apply_warm_background(s2)
    add_header(s2, "核心命題與定義界定：Agent = Model + Harness", "理論基礎", "破解模型至上神話，確立 Runtime、Scaffold、Framework 與 Orchestrator 的嚴格邊界")
    
    add_enlarged_bullet_card(
        s2, left=0.8, top=1.75, width=5.7, height=4.1,
        title="1. 破解模型至上論 (The Model Myth)",
        items=[
            "核心公式等式：Agent = Model + Harness，兩者相乘而非相加。",
            "模型僅提供機率符號：LLM 本質是無狀態、易幻覺的預測引擎。",
            "Harness 提供確定性實踐：負責負載環境狀態管理、工具排程與生命週期掌控。",
            "軟體工程交付關鍵：工程交付失敗，90% 源於 Harness 脆弱而非模型推理不足。"
        ],
        tag="CORE THESIS",
        accent_color=BRAND_SAGE
    )
    add_enlarged_bullet_card(
        s2, left=6.833, top=1.75, width=5.7, height=4.1,
        title="2. 四大混淆術語邊界澄清 (Clarifying Terms)",
        items=[
            "Harness vs Scaffold (腳手架)：Scaffold 僅是引導輸出的靜態 Prompt；Harness 是掌控生命週期的動態運行時 (Runtime)。",
            "Harness vs Framework (如 LangChain)：Framework 提供通用庫抽象；Harness 是特化、高確定性的全棧編程產品本體。",
            "Harness vs Eval Harness (如 SWE-bench)：評測框架是外部評判裁判；Coding Harness 才是受測的軟體實體自身。",
            "Harness vs Orchestrator (協調器)：Orchestrator 僅負責跨模組派工；Harness 包含重試、沙盒與檔案編輯的完整垂直底座。"
        ],
        tag="TAXONOMY",
        accent_color=BRAND_TERRA
    )
    add_centered_quote_card(
        s2, left=0.8, top=6.0, width=11.733, height=0.95,
        en_quote="The model supplies the intelligence, but the harness turns that intelligence into reliable work.",
        highlight_word="turns that intelligence into reliable work",
        zh_quote="模型賦予原始智慧，而執行框架（Harness）則將智慧轉化為高可靠、可預測的工程成果。"
    )
    add_footer(s2, 2)

    # --------------------------------------------------------------------------
    # SLIDE 3: 【重繪論文圖一】D1-D7 標準子系統架構圖 (Figure 1 Re-drawn)
    # --------------------------------------------------------------------------
    s3 = prs.slides.add_slide(blank_layout)
    apply_warm_background(s3)
    add_header(s3, "【重繪論文圖一】Harness 七大標準子系統架構全景", "論文圖一重繪", "Figure 1: The Canonical Anatomy and Architecture of Coding Agent Harnesses")
    
    # Outer container representing the Harness boundary
    harness_box = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.75), Inches(11.733), Inches(5.2))
    harness_box.fill.solid()
    harness_box.fill.fore_color.rgb = BG_CARD
    harness_box.line.color.rgb = BRAND_SAGE
    harness_box.line.width = Pt(1.5)
    
    # Harness Title Banner inside
    h_label = s3.shapes.add_textbox(Inches(1.0), Inches(1.85), Inches(11.333), Inches(0.35))
    tf_hl = h_label.text_frame
    p_hl = tf_hl.paragraphs[0]
    r_hl = p_hl.add_run()
    r_hl.text = "THE EXECUTION HARNESS RUNTIME BOUNDARY (AI-ROS 運行時架構邊界)"
    r_hl.font.name = FONT_HEADING
    r_hl.font.size = Pt(11)
    r_hl.font.bold = True
    r_hl.font.color.rgb = BRAND_SAGE
    
    # Top Level: D1 Agent Loop
    d1_card = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.1), Inches(2.25), Inches(11.133), Inches(0.95))
    d1_card.fill.solid()
    d1_card.fill.fore_color.rgb = RGBColor(0xEA, 0xF0, 0xEC)
    d1_card.line.color.rgb = BRAND_SAGE
    d1_card.line.width = Pt(1.2)
    tf_d1 = d1_card.text_frame
    tf_d1.margin_left = tf_d1.margin_top = tf_d1.margin_right = tf_d1.margin_bottom = 0
    p_d1 = tf_d1.paragraphs[0]
    p_d1.alignment = PP_ALIGN.CENTER
    r_d1 = p_d1.add_run()
    r_d1.text = "D1. Agent Loop (核心驅動引擎 / 狀態機迴圈)\n"
    r_d1.font.name = FONT_HEADING
    r_d1.font.size = Pt(11.5)
    r_d1.font.bold = True
    r_d1.font.color.rgb = BRAND_SLATE
    r_d1_sub = p_d1.add_run()
    r_d1_sub.text = "ReAct / Coordinator-Worker · 死循環偵測 (Stuck Detectors) · 逾時中斷 · 中間件管線 (Middleware Pipeline)"
    r_d1_sub.font.name = FONT_BODY
    r_d1_sub.font.size = Pt(10)
    r_d1_sub.font.color.rgb = TEXT_BODY
    
    # Middle Row: D2, D4, D3 (Three core operational pillars)
    mid_w = 3.55
    mid_gap = 0.24
    
    # D2
    d2_card = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.1), Inches(3.35), Inches(mid_w), Inches(1.6))
    d2_card.fill.solid()
    d2_card.fill.fore_color.rgb = BG_CANVAS
    d2_card.line.color.rgb = BORDER_CARD
    d2_card.line.width = Pt(1)
    tf_d2 = d2_card.text_frame
    p_d2_t = tf_d2.paragraphs[0]
    p_d2_t.alignment = PP_ALIGN.CENTER
    r_d2_t = p_d2_t.add_run()
    r_d2_t.text = "D2. 模型整合與協同\n"
    r_d2_t.font.name = FONT_HEADING
    r_d2_t.font.size = Pt(11)
    r_d2_t.font.bold = True
    r_d2_t.font.color.rgb = BRAND_TERRA
    p_d2_b = tf_d2.add_paragraph()
    p_d2_b.space_before = Pt(4)
    r_d2_b = p_d2_b.add_run()
    r_d2_b.text = "✦ 單原廠深度優化 vs 多模型抽象\n✦ 嚴格 Prompt Caching 快取邊界\n✦ 反鍍金規則 (Anti-Gold-Plating)\n✦ 結構化推理與 API 轉譯層"
    r_d2_b.font.name = FONT_BODY
    r_d2_b.font.size = Pt(9.5)
    r_d2_b.font.color.rgb = TEXT_BODY
    
    # D4
    d4_card = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.1 + mid_w + mid_gap), Inches(3.35), Inches(mid_w), Inches(1.6))
    d4_card.fill.solid()
    d4_card.fill.fore_color.rgb = BG_CANVAS
    d4_card.line.color.rgb = BORDER_CARD
    d4_card.line.width = Pt(1)
    tf_d4 = d4_card.text_frame
    p_d4_t = tf_d4.paragraphs[0]
    p_d4_t.alignment = PP_ALIGN.CENTER
    r_d4_t = p_d4_t.add_run()
    r_d4_t.text = "D4. 記憶與上下文管理\n"
    r_d4_t.font.name = FONT_HEADING
    r_d4_t.font.size = Pt(11)
    r_d4_t.font.bold = True
    r_d4_t.font.color.rgb = BRAND_SAGE
    p_d4_b = tf_d4.add_paragraph()
    p_d4_b.space_before = Pt(4)
    r_d4_b = p_d4_b.add_run()
    r_d4_b.text = "✦ 閾值壓縮 (Threshold Compaction)\n✦ 非破壞性修剪 (Micro-pruning)\n✦ 保留最近 30% 完整推理尾端\n✦ 磁碟外生化狀態持久儲存"
    r_d4_b.font.name = FONT_BODY
    r_d4_b.font.size = Pt(9.5)
    r_d4_b.font.color.rgb = TEXT_BODY
    
    # D3
    d3_card = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.1 + (mid_w + mid_gap)*2), Inches(3.35), Inches(mid_w), Inches(1.6))
    d3_card.fill.solid()
    d3_card.fill.fore_color.rgb = BG_CANVAS
    d3_card.line.color.rgb = BORDER_CARD
    d3_card.line.width = Pt(1)
    tf_d3 = d3_card.text_frame
    p_d3_t = tf_d3.paragraphs[0]
    p_d3_t.alignment = PP_ALIGN.CENTER
    r_d3_t = p_d3_t.add_run()
    r_d3_t.text = "D3. 工具與動作系統\n"
    r_d3_t.font.name = FONT_HEADING
    r_d3_t.font.size = Pt(11)
    r_d3_t.font.bold = True
    r_d3_t.font.color.rgb = BRAND_OCHRE
    p_d3_b = tf_d3.add_paragraph()
    p_d3_b.space_before = Pt(4)
    r_d3_b = p_d3_b.add_run()
    r_d3_b.text = "✦ 精簡 4~8 個核心確定性工具\n✦ Search-Replace 區塊精確替換\n✦ 模糊匹配寬容瀑布 (Fuzzy 95%)\n✦ 逾 15 個工具啟用遞延加載"
    r_d3_b.font.name = FONT_BODY
    r_d3_b.font.size = Pt(9.5)
    r_d3_b.font.color.rgb = TEXT_BODY
    
    # Bottom Row: D5, D6, D7 (Governance, Topology, Ecosystem)
    d5_card = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.1), Inches(5.1), Inches(mid_w), Inches(1.65))
    d5_card.fill.solid()
    d5_card.fill.fore_color.rgb = BG_CANVAS
    d5_card.line.color.rgb = BORDER_CARD
    d5_card.line.width = Pt(1)
    tf_d5 = d5_card.text_frame
    p_d5_t = tf_d5.paragraphs[0]
    p_d5_t.alignment = PP_ALIGN.CENTER
    r_d5_t = p_d5_t.add_run()
    r_d5_t.text = "D5. 安全與權限棧\n"
    r_d5_t.font.name = FONT_HEADING
    r_d5_t.font.size = Pt(11)
    r_d5_t.font.bold = True
    r_d5_t.font.color.rgb = BRAND_TERRA
    p_d5_b = tf_d5.add_paragraph()
    p_d5_b.space_before = Pt(4)
    r_d5_b = p_d5_b.add_run()
    r_d5_b.text = "✦ Starlark 腳本與可執行測試案例\n✦ 外部守護模型 (Guardian Review)\n✦ 容器與 OS 級沙盒隔離 (Bwrap)\n✦ 高危動作人機審查 (HITL)"
    r_d5_b.font.name = FONT_BODY
    r_d5_b.font.size = Pt(9.5)
    r_d5_b.font.color.rgb = TEXT_BODY
    
    d6_card = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.1 + mid_w + mid_gap), Inches(5.1), Inches(mid_w), Inches(1.65))
    d6_card.fill.solid()
    d6_card.fill.fore_color.rgb = BG_CANVAS
    d6_card.line.color.rgb = BORDER_CARD
    d6_card.line.width = Pt(1)
    tf_d6 = d6_card.text_frame
    p_d6_t = tf_d6.paragraphs[0]
    p_d6_t.alignment = PP_ALIGN.CENTER
    r_d6_t = p_d6_t.add_run()
    r_d6_t.text = "D6. 多代理協同拓撲\n"
    r_d6_t.font.name = FONT_HEADING
    r_d6_t.font.size = Pt(11)
    r_d6_t.font.bold = True
    r_d6_t.font.color.rgb = BRAND_SAGE
    p_d6_b = tf_d6.add_paragraph()
    p_d6_b.space_before = Pt(4)
    r_d6_b = p_d6_b.add_run()
    r_d6_b.text = "✦ 嚴禁平面 Chat-Room 廣播\n✦ 遞迴組合 (Recursive Sub-Agents)\n✦ 線程樹 (Thread Trees) 支援回滾\n✦ 保持進程內通訊避免 RPC 膨脹"
    r_d6_b.font.name = FONT_BODY
    r_d6_b.font.size = Pt(9.5)
    r_d6_b.font.color.rgb = TEXT_BODY
    
    d7_card = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.1 + (mid_w + mid_gap)*2), Inches(5.1), Inches(mid_w), Inches(1.65))
    d7_card.fill.solid()
    d7_card.fill.fore_color.rgb = BG_CANVAS
    d7_card.line.color.rgb = BORDER_CARD
    d7_card.line.width = Pt(1)
    tf_d7 = d7_card.text_frame
    p_d7_t = tf_d7.paragraphs[0]
    p_d7_t.alignment = PP_ALIGN.CENTER
    r_d7_t = p_d7_t.add_run()
    r_d7_t.text = "D7. 擴展與技能體系\n"
    r_d7_t.font.name = FONT_HEADING
    r_d7_t.font.size = Pt(11)
    r_d7_t.font.bold = True
    r_d7_t.font.color.rgb = BRAND_SLATE
    p_d7_b = tf_d7.add_paragraph()
    p_d7_b.space_before = Pt(4)
    r_d7_b = p_d7_b.add_run()
    r_d7_b.text = "✦ SKILL.md 領域知識標準 (9/11)\n✦ MCP 外部系統連網協議 (8/11)\n✦ 遞延動態加載省 90% 提示詞空間\n✦ 外掛生命週期 Hooks (Pre/Post)"
    r_d7_b.font.name = FONT_BODY
    r_d7_b.font.size = Pt(9.5)
    r_d7_b.font.color.rgb = TEXT_BODY
    
    add_footer(s3, 3)

    # --------------------------------------------------------------------------
    # SLIDE 4: 11 款審查對象矩陣 (Table 1: Corpus of 11 Production Systems)
    # --------------------------------------------------------------------------
    s4 = prs.slides.add_slide(blank_layout)
    apply_warm_background(s4)
    add_header(s4, "審查對象全景矩陣：11 款一線生產系統與 1 款元框架", "實證樣本", "涵蓋模型原廠旗艦、開源領航者、極簡主義反動與企業級 Meta-Harness")
    
    headers_s4 = ["系統名稱", "組織/作者", "語言", "定位", "核心架構亮點與論文實證結論"]
    rows_s4 = [
        ["Claude Code", "Anthropic", "TS", "原廠旗艦", "深度 Prompt Caching、單原廠垂直優化、遞迴子代理、三層權限防禦"],
        ["Codex CLI", "OpenAI", "Rust", "原廠原生", "高效能原生二進位、Starlark 策略、線程樹協同、Bubblewrap 沙盒"],
        ["Gemini CLI", "Google", "TS", "原廠終端", "巨量 Context 窗口優化、三模式權限 (Plan/Default/YOLO)、跳過自身 ADK"],
        ["Mistral Vibe", "Mistral AI", "Python", "原廠輕量", "中間件管線迴圈、精確子字串替換、原廠模型優先 + 通用 Fallback"],
        ["OpenHands", "All-Hands", "Python", "開源主機", "事件溯源 (Event-Sourcing)、Docker 容器沙盒、支援外部外掛生態"],
        ["Aider", "P. Gauthier", "Python", "Git 配對", "反思增強迴圈 (Linter)、多型語法 Diff (4 種編輯器)、極簡 Token 消耗"],
        ["OpenCode", "OpenCode", "TS", "星數最高", "Client/Server 架構、日誌即工作佇列、九階模糊寬容補丁瀑布"],
        ["Hermes", "Nous Res.", "Python", "快速成長", "SQLite FTS5 記憶索引、自我改進技能迴圈 (Self-improving Loop)"],
        ["Pi", "M. Zechner", "TS", "極簡主義", "微核心反過度工程、零冗餘依賴、每輪 Token 成本與快取浪費稽核"],
        ["Mini-SWE", "SWE 團隊", "Python", "極簡基線", "僅 100 行線形迴圈，揭示 SWE-bench 高分與框架複雜度脫鉤事實"],
        ["OpenClaw", "OpenClaw", "Go", "通訊網關", "高併發通訊管道分發、事件橋接、以獨立外掛調度編程代理"],
        ["Omnigent", "Databricks", "Python", "元框架", "Meta-Harness 對比點：以統一 API 調度 11 家原廠 Harness，消除鎖定"]
    ]
    col_w_s4 = [1.8, 1.5, 1.0, 1.4, 6.033]
    create_enlarged_table(s4, left=0.8, top=1.75, width=11.733, height=5.2, headers=headers_s4, rows_data=rows_s4, col_widths=col_w_s4, font_size=8.5)
    add_footer(s4, 4)

    # --------------------------------------------------------------------------
    # SLIDE 5: 【重繪論文圖二】三種驅動迴圈範式對比 (Figure 2 Re-drawn)
    # --------------------------------------------------------------------------
    s5 = prs.slides.add_slide(blank_layout)
    apply_warm_background(s5)
    add_header(s5, "【重繪論文圖二】三種驅動迴圈範式對比 (Figure 2)", "迴圈架構", "Figure 2: Contrasting Iterative ReAct, Reflection-Augmented, and Coordinator-Worker Loops")
    
    col3_w = 3.75
    col3_gap = 0.24
    
    # Paradigm 1: Iterative Loop
    p1 = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.75), Inches(col3_w), Inches(5.2))
    p1.fill.solid()
    p1.fill.fore_color.rgb = BG_CARD
    p1.line.color.rgb = BORDER_CARD
    p1.line.width = Pt(1)
    
    tb_p1 = s5.shapes.add_textbox(Inches(1.0), Inches(1.9), Inches(col3_w - 0.4), Inches(4.9))
    tf_p1 = tb_p1.text_frame
    tf_p1.word_wrap = True
    p1_0 = tf_p1.paragraphs[0]
    r_p1_0 = p1_0.add_run()
    r_p1_0.text = "範式 1: 迭代動作迴圈\n(Iterative ReAct Loop)\n"
    r_p1_0.font.name = FONT_HEADING
    r_p1_0.font.size = Pt(12)
    r_p1_0.font.bold = True
    r_p1_0.font.color.rgb = BRAND_SAGE
    
    p1_sub = tf_p1.add_paragraph()
    r_p1_sub = p1_sub.add_run()
    r_p1_sub.text = "代表系統：Mini-SWE-Agent, OpenHands, OpenCode, Pi\n"
    r_p1_sub.font.name = FONT_BODY
    r_p1_sub.font.size = Pt(9.5)
    r_p1_sub.font.color.rgb = BRAND_TERRA
    
    p1_flow = tf_p1.add_paragraph()
    p1_flow.space_before = Pt(8)
    r_flow1 = p1_flow.add_run()
    r_flow1.text = "【控制流程圖解】\n[User Input] ➔ Prompt 組裝\n       ▼\n[LLM Completion] 推理預測\n       ▼\n[Tool Execution] 本地執行\n       ▼\n[Observation] 狀態反饋\n       ▼\n[Compaction / Stuck Check]\n       ▼ 循環直到 Stop Token\n\n✦ 優點：極簡、開銷低、狀態直觀\n✦ 缺點：缺乏自校正、易陷入死循環"
    r_flow1.font.name = FONT_BODY
    r_flow1.font.size = Pt(10)
    r_flow1.font.color.rgb = TEXT_BODY
    
    # Paradigm 2: Reflection-Augmented
    p2 = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8 + col3_w + col3_gap), Inches(1.75), Inches(col3_w), Inches(5.2))
    p2.fill.solid()
    p2.fill.fore_color.rgb = BG_CARD
    p2.line.color.rgb = BORDER_CARD
    p2.line.width = Pt(1)
    
    tb_p2 = s5.shapes.add_textbox(Inches(1.0 + col3_w + col3_gap), Inches(1.9), Inches(col3_w - 0.4), Inches(4.9))
    tf_p2 = tb_p2.text_frame
    tf_p2.word_wrap = True
    p2_0 = tf_p2.paragraphs[0]
    r_p2_0 = p2_0.add_run()
    r_p2_0.text = "範式 2: 反思增強迴圈\n(Reflection-Augmented Loop)\n"
    r_p2_0.font.name = FONT_HEADING
    r_p2_0.font.size = Pt(12)
    r_p2_0.font.bold = True
    r_p2_0.font.color.rgb = BRAND_TERRA
    
    p2_sub = tf_p2.add_paragraph()
    r_p2_sub = p2_sub.add_run()
    r_p2_sub.text = "代表系統：Aider (run_one 核心), Hermes (Verify Guard)\n"
    r_p2_sub.font.name = FONT_BODY
    r_p2_sub.font.size = Pt(9.5)
    r_p2_sub.font.color.rgb = BRAND_SAGE
    
    p2_flow = tf_p2.add_paragraph()
    p2_flow.space_before = Pt(8)
    r_flow2 = p2_flow.add_run()
    r_flow2.text = "【控制流程圖解】\n[LLM Edit Response]\n       ▼\n[Apply Diff Patch]\n       ▼\n[Run Linter & AST Syntax]\n       ▼\n[Run Test Suite (測試集)]\n       ▼ 失敗？\n[Reflected Feedback] 注入錯誤訊號\n       ▼ 重新請求 LLM (最多 3 次)\n\n✦ 優點：產出代碼零語法錯誤\n✦ 缺點：耗費額外 Token 與執行時間"
    r_flow2.font.name = FONT_BODY
    r_flow2.font.size = Pt(10)
    r_flow2.font.color.rgb = TEXT_BODY
    
    # Paradigm 3: Coordinator-Worker
    p3 = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8 + (col3_w + col3_gap)*2), Inches(1.75), Inches(col3_w), Inches(5.2))
    p3.fill.solid()
    p3.fill.fore_color.rgb = BG_CARD
    p3.line.color.rgb = BORDER_CARD
    p3.line.width = Pt(1)
    
    tb_p3 = s5.shapes.add_textbox(Inches(1.0 + (col3_w + col3_gap)*2), Inches(1.9), Inches(col3_w - 0.4), Inches(4.9))
    tf_p3 = tb_p3.text_frame
    tf_p3.word_wrap = True
    p3_0 = tf_p3.paragraphs[0]
    r_p3_0 = p3_0.add_run()
    r_p3_0.text = "範式 3: 協調工兵派工\n(Coordinator-Worker Pattern)\n"
    r_p3_0.font.name = FONT_HEADING
    r_p3_0.font.size = Pt(12)
    r_p3_0.font.bold = True
    r_p3_0.font.color.rgb = BRAND_OCHRE
    
    p3_sub = tf_p3.add_paragraph()
    r_p3_sub = p3_sub.add_run()
    r_p3_sub.text = "代表系統：Claude Code, Codex, Gemini CLI, Hermes Swarm\n"
    r_p3_sub.font.name = FONT_BODY
    r_p3_sub.font.size = Pt(9.5)
    r_p3_sub.font.color.rgb = BRAND_SLATE
    
    p3_flow = tf_p3.add_paragraph()
    p3_flow.space_before = Pt(8)
    r_flow3 = p3_flow.add_run()
    r_flow3.text = "【控制流程圖解】\n[Lead Coordinator] 接收總目標\n       ▼ 拆解為獨立子任務\n[Fork Sub-Agent Context]\n       ▼\n[Worker 1]    [Worker 2]    [Worker 3]\n(專門檢索)    (執行編譯)    (審核修改)\n       ▼             ▼             ▼\n[Task-Notification XML 摘要回傳]\n       ▼\n[Lead 合成結果並進入下一階段]\n\n✦ 優點：保護主 Context、並行探索\n✦ 缺點：協調複雜度高、Token 開銷大"
    r_flow3.font.name = FONT_BODY
    r_flow3.font.size = Pt(10)
    r_flow3.font.color.rgb = TEXT_BODY
    
    add_footer(s5, 5)

    # --------------------------------------------------------------------------
    # SLIDE 6: D1 驅動迴圈進階實踐 (Loop Engineering & Stuck Detectors)
    # --------------------------------------------------------------------------
    s6 = prs.slides.add_slide(blank_layout)
    apply_warm_background(s6)
    add_header(s6, "D1 驅動迴圈工程：死循環偵測、逾時防護與中間件管線", "子系統深度", "從單純 While-Loop 到工業級強固控制流，確保長程自主任務不脫軌")
    
    add_enlarged_bullet_card(
        s6, left=0.8, top=1.75, width=5.7, height=4.2,
        title="1. 死循環與震盪偵測器 (Stuck Detectors)",
        items=[
            "呼叫雜湊比對 (Signature Hashing)：即時記錄模型產生的工具名稱與參數雜湊。",
            "連續重複攔截：當偵測到連續 3 次執行完全相同的指令且失敗，立刻中斷自動執行。",
            "人機介入升級 (Permission Escalation)：如 OpenCode 將重複呼叫轉為 doom_loop 權限詢問。",
            "自適應修正注入：強制中斷模型思維鏈，向 Context 注入「請停止重複，嘗試替代方案」約束。"
        ],
        tag="STUCK PREVENTION",
        accent_color=BRAND_SAGE
    )
    add_enlarged_bullet_card(
        s6, left=6.833, top=1.75, width=5.7, height=4.2,
        title="2. 中間件架構與異常復原 (Middleware Pipeline)",
        items=[
            "中間件解耦 (Mistral Vibe 模式)：將輪數上限、預算監控、唯讀模式抽離為獨立中間件。",
            "截斷毒害防護 (Truncation-Poisoning Guard)：當輸出遭長度截斷時，強制拒絕部分工具執行。",
            "暫態錯誤重試白名單：針對網路波動、API 429 等預設 40 餘種模式指數退避重試。",
            "溢位即壓縮 (Compact-on-Overflow)：遇到 Context 長度超限立即觸發壓縮，而非直接報錯退回。"
        ],
        tag="RECOVERY PIPELINE",
        accent_color=BRAND_TERRA
    )
    add_centered_quote_card(
        s6, left=0.8, top=6.05, width=11.733, height=0.9,
        en_quote="Do not over-engineer stuck detection, but do ship cheap caps: they cost a dozen lines and save hundreds of dollars.",
        highlight_word="ship cheap caps",
        zh_quote="切勿過度設計複雜的卡死偵測，但務必實作輕量計數上限：十幾行代碼即可避免數百美元的 Token 浪費。"
    )
    add_footer(s6, 6)

    # --------------------------------------------------------------------------
    # SLIDE 7: D2 模型深度整合：Prompt Caching 與反鍍金
    # --------------------------------------------------------------------------
    s7 = prs.slides.add_slide(blank_layout)
    apply_warm_background(s7)
    add_header(s7, "D2 模型整合與協同：Prompt Caching 快取對齊與反鍍金規則", "子系統深度", "深入原廠 API 物理特性，壓降 80% 延遲並根絕 AI 廢話與過度工程")
    
    add_enlarged_bullet_card(
        s7, left=0.8, top=1.75, width=5.7, height=4.2,
        title="1. Prompt Caching 邊界對齊藝術",
        items=[
            "靜態與動態嚴格分離：將系統提示詞、工具定義等靜態內容固定於前綴，確保快取命中率 >90%。",
            "快取失效審計 (Cache-Miss Dollar Waste)：如 Pi 系統將每次快取失效量化為美元損失以供優化。",
            "子代理快取繼承：Claude Code 在 Fork 子代理時，原封不動拷貝父級 renderedSystemPrompt 凍結快取。",
            "模型調度分流：輕量階段（如搜尋、摘要）調用 Haiku/Flash，寫碼與架構才使用 Frontier 主力模型。"
        ],
        tag="CACHE ALIGNMENT",
        accent_color=BRAND_SAGE
    )
    add_enlarged_bullet_card(
        s7, left=6.833, top=1.75, width=5.7, height=4.2,
        title="2. 反鍍金規則 (Anti-Gold-Plating Rules)",
        items=[
            "負面約束密集注入：原廠 Prompt 明確禁止「重構非必要代碼」、「額外增添抽象層」。",
            "禁止重複造輪子：禁止自行實現已知庫函式，強烈要求直接呼叫既有依賴。",
            "消除說教與寒暄：嚴禁模型輸出「好的，我現在為您...」等無效客套 Token，直出 Tool Call。",
            "省下 35% Token 浪費：實證研究顯示，嚴格的反鍍金指令能立竿見影地降低整體開發成本。"
        ],
        tag="ANTI-GOLD-PLATING",
        accent_color=BRAND_TERRA
    )
    add_centered_quote_card(
        s7, left=0.8, top=6.05, width=11.733, height=0.9,
        en_quote="Anti-gold-plating instructions are the unsung heroes of coding prompts, cutting token waste by 35%.",
        highlight_word="Anti-gold-plating instructions",
        zh_quote="反鍍金指令是編程提示詞的無名英雄，有效消減了 35% 以上的無意義 Token 浪費。"
    )
    add_footer(s7, 7)

    # --------------------------------------------------------------------------
    # SLIDE 8: D3 工具與動作系統：多型代碼編輯策略
    # --------------------------------------------------------------------------
    s8 = prs.slides.add_slide(blank_layout)
    apply_warm_background(s8)
    add_header(s8, "D3 工具系統：確定性微工具與多型代碼編輯演進", "子系統深度", "徹底淘汰整檔重寫，確立 Search-and-Replace 與語法寬容補丁標準")
    
    add_enlarged_bullet_card(
        s8, left=0.8, top=1.75, width=5.7, height=5.2,
        title="1. 確定性微工具集收斂",
        items=[
            "工具數量收斂：一線系統核心原生工具極度精簡，普遍維持在 4～8 個（ReadFile, Edit, RunBash, Grep）。",
            "超過 15 個工具啟用遞延加載：使用 shouldDefer 標記與 ToolSearch，縮減 40% 提示詞空間。",
            "沙盒化串流執行：終端指令 (Bash) 透過管道受控執行，具備超時中斷與輸出截斷保護。",
            "語意化報錯反饋：工具出錯時回傳 Exit Code 與 Stderr 前 5 行，引導模型自行除錯修復。"
        ],
        tag="TOOL CONVERGENCE",
        accent_color=BRAND_SAGE
    )
    add_enlarged_bullet_card(
        s8, left=6.833, top=1.75, width=5.7, height=5.2,
        title="2. 檔案編輯策略光譜 (Editing Spectrum)",
        items=[
            "淘汰整檔重寫 (Whole-file rewrite)：高並發易丟失代碼、破壞縮排，且巨幅浪費 Token。",
            "主流方案：精確唯一子字串替換 (Search-and-Replace) 與 Aider 多型 Unified Diff。",
            "模糊匹配寬容瀑布 (Fuzzy Matching Cascade)：縮排或空白偏差時自動啟用 Levenshtein 距離比對。",
            "補丁命中率躍升至 95%：模糊寬容機制徹底解決模型在程式碼行號飄移時套用失敗的難題。",
            "即時語法校驗：寫入磁碟後背景即時觸發 AST 與 Linter 檢查，杜絕殘缺代碼提交。"
        ],
        tag="FILE EDITING",
        accent_color=BRAND_TERRA
    )
    add_footer(s8, 8)

    # --------------------------------------------------------------------------
    # SLIDE 9: 【重繪論文圖四】四種記憶與上下文管理策略 (Figure 4 Re-drawn)
    # --------------------------------------------------------------------------
    s9 = prs.slides.add_slide(blank_layout)
    apply_warm_background(s9)
    add_header(s9, "【重繪論文圖四】四種記憶與上下文管理策略 (Figure 4)", "記憶架構", "Figure 4: Four Practical Context Management Strategies in Increasing Sophistication")
    
    col4_w = 2.75
    col4_gap = 0.24
    
    # Strategy 1: Linear History
    c1 = s9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.75), Inches(col4_w), Inches(5.2))
    c1.fill.solid()
    c1.fill.fore_color.rgb = BG_CARD
    c1.line.color.rgb = BORDER_CARD
    c1.line.width = Pt(1)
    tb_c1 = s9.shapes.add_textbox(Inches(0.95), Inches(1.9), Inches(col4_w - 0.3), Inches(4.9))
    tf_c1 = tb_c1.text_frame
    tf_c1.word_wrap = True
    p = tf_c1.paragraphs[0]
    r = p.add_run()
    r.text = "策略 1: 線性歷史\n(Linear History)\n"
    r.font.name = FONT_HEADING
    r.font.size = Pt(11.5)
    r.font.bold = True
    r.font.color.rgb = BRAND_SAGE
    p_sub = tf_c1.add_paragraph()
    r_sub = p_sub.add_run()
    r_sub.text = "代表系統：Mini-SWE-Agent\n"
    r_sub.font.name = FONT_BODY
    r_sub.font.size = Pt(9)
    r_sub.font.color.rgb = BRAND_TERRA
    p_body = tf_c1.add_paragraph()
    p_body.space_before = Pt(6)
    r_body = p_body.add_run()
    r_body.text = "【架構原理】\n對話列表無限制線性成長，完全仰賴現代 LLM 具備之原生超長上下文窗口 (如 Claude 1M)。\n\n✦ 適用場景：短期評測、基準研究\n✦ 核心優勢：軌跡 100% 可復現\n✦ 嚴重缺陷：長程任務必爆發注意力衰退與 Token 費用失控"
    r_body.font.name = FONT_BODY
    r_body.font.size = Pt(9.5)
    r_body.font.color.rgb = TEXT_BODY
    
    # Strategy 2: Recursive Halving Summarization
    c2 = s9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8 + col4_w + col4_gap), Inches(1.75), Inches(col4_w), Inches(5.2))
    c2.fill.solid()
    c2.fill.fore_color.rgb = BG_CARD
    c2.line.color.rgb = BORDER_CARD
    c2.line.width = Pt(1)
    tb_c2 = s9.shapes.add_textbox(Inches(0.95 + col4_w + col4_gap), Inches(1.9), Inches(col4_w - 0.3), Inches(4.9))
    tf_c2 = tb_c2.text_frame
    tf_c2.word_wrap = True
    p = tf_c2.paragraphs[0]
    r = p.add_run()
    r.text = "策略 2: 遞迴二分摘要\n(Recursive Halving)\n"
    r.font.name = FONT_HEADING
    r.font.size = Pt(11.5)
    r.font.bold = True
    r.font.color.rgb = BRAND_TERRA
    p_sub = tf_c2.add_paragraph()
    r_sub = p_sub.add_run()
    r_sub.text = "代表系統：Aider (ChatSummary)\n"
    r_sub.font.name = FONT_BODY
    r_sub.font.size = Pt(9)
    r_sub.font.color.rgb = BRAND_SAGE
    p_body = tf_c2.add_paragraph()
    p_body.space_before = Pt(6)
    r_body = p_body.add_run()
    r_body.text = "【架構原理】\n當 Token 超過門檻 (預設 1024)，將歷史平分為前後兩半：保留最近 50% 尾端，將前半段以弱模型進行遞迴摘要。\n\n✦ 適用場景：Git 配對編程\n✦ 核心優勢：近期推導完整不失真\n✦ 缺陷：遞迴壓縮可能丟失深層歷史架構因果關係"
    r_body.font.name = FONT_BODY
    r_body.font.size = Pt(9.5)
    r_body.font.color.rgb = TEXT_BODY
    
    # Strategy 3: Pluggable Condensation
    c3 = s9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8 + (col4_w + col4_gap)*2), Inches(1.75), Inches(col4_w), Inches(5.2))
    c3.fill.solid()
    c3.fill.fore_color.rgb = BG_CARD
    c3.line.color.rgb = BORDER_CARD
    c3.line.width = Pt(1)
    tb_c3 = s9.shapes.add_textbox(Inches(0.95 + (col4_w + col4_gap)*2), Inches(1.9), Inches(col4_w - 0.3), Inches(4.9))
    tf_c3 = tb_c3.text_frame
    tf_c3.word_wrap = True
    p = tf_c3.paragraphs[0]
    r = p.add_run()
    r.text = "策略 3: 可插拔壓縮器\n(Pluggable Condenser)\n"
    r.font.name = FONT_HEADING
    r.font.size = Pt(11.5)
    r.font.bold = True
    r.font.color.rgb = BRAND_OCHRE
    p_sub = tf_c3.add_paragraph()
    r_sub = p_sub.add_run()
    r_sub.text = "代表系統：OpenHands SDK\n"
    r_sub.font.name = FONT_BODY
    r_sub.font.size = Pt(9)
    r_sub.font.color.rgb = BRAND_SLATE
    p_body = tf_c3.add_paragraph()
    p_body.space_before = Pt(6)
    r_body = p_body.add_run()
    r_body.text = "【架構原理】\n抽象出 Condenser 基底類別，整合事件溯源 (Event-Sourcing)，壓縮操作本身即為可重放事件；兼作溢位復原機制。\n\n✦ 適用場景：長程自主 Agent 主機\n✦ 核心優勢：支援管線化多級壓縮\n✦ 演化反思：V1 將過度設計的 10 種精簡為 3 種核心實作"
    r_body.font.name = FONT_BODY
    r_body.font.size = Pt(9.5)
    r_body.font.color.rgb = TEXT_BODY
    
    # Strategy 4: Threshold Compaction
    c4 = s9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8 + (col4_w + col4_gap)*3), Inches(1.75), Inches(col4_w), Inches(5.2))
    c4.fill.solid()
    c4.fill.fore_color.rgb = BG_CARD
    c4.line.color.rgb = BORDER_CARD
    c4.line.width = Pt(1)
    tb_c4 = s9.shapes.add_textbox(Inches(0.95 + (col4_w + col4_gap)*3), Inches(1.9), Inches(col4_w - 0.3), Inches(4.9))
    tf_c4 = tb_c4.text_frame
    tf_c4.word_wrap = True
    p = tf_c4.paragraphs[0]
    r = p.add_run()
    r.text = "策略 4: 閾值邊界壓縮\n(Threshold Compaction)\n"
    r.font.name = FONT_HEADING
    r.font.size = Pt(11.5)
    r.font.bold = True
    r.font.color.rgb = BRAND_SLATE
    p_sub = tf_c4.add_paragraph()
    r_sub = p_sub.add_run()
    r_sub.text = "代表系統：Claude Code, Codex, Gemini CLI\n"
    r_sub.font.name = FONT_BODY
    r_sub.font.size = Pt(9)
    r_sub.font.color.rgb = BRAND_SAGE
    p_body = tf_c4.add_paragraph()
    p_body.space_before = Pt(6)
    r_body = p_body.add_run()
    r_body.text = "【架構原理】\n當 Token 逼近模型有效邊界 (如預留 13K Buffer) 時觸發：(1) 剝離圖片與冗餘日誌，(2) 結構化總結，(3) 建立邊界訊息，(4) 還原關鍵檔案。\n\n✦ 適用場景：工業級生產 CLI 旗艦\n✦ 核心優勢：無感維持訊號純淨度\n✦ 確立為 2026 年底事實標準"
    r_body.font.name = FONT_BODY
    r_body.font.size = Pt(9.5)
    r_body.font.color.rgb = TEXT_BODY
    
    add_footer(s9, 9)

    # --------------------------------------------------------------------------
    # SLIDE 10: 【重繪論文圖五】Claude Code 與 Codex 安全防禦架構 (Figure 5 Re-drawn)
    # --------------------------------------------------------------------------
    s10 = prs.slides.add_slide(blank_layout)
    apply_warm_background(s10)
    add_header(s10, "【重繪論文圖五】Claude Code 與 Codex 安全防禦棧 (Figure 5)", "安全架構", "Figure 5: Multi-Layered Permission Stacks and Sandboxing in Tier-1 Harnesses")
    
    # Left Box: Claude Code 3 Layers
    box_cl = s10.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.75), Inches(5.7), Inches(5.2))
    box_cl.fill.solid()
    box_cl.fill.fore_color.rgb = BG_CARD
    box_cl.line.color.rgb = BORDER_CARD
    box_cl.line.width = Pt(1)
    
    tb_cl = s10.shapes.add_textbox(Inches(1.0), Inches(1.9), Inches(5.3), Inches(4.9))
    tf_cl = tb_cl.text_frame
    tf_cl.word_wrap = True
    p = tf_cl.paragraphs[0]
    r = p.add_run()
    r.text = "Claude Code: 優雅的三層權限防禦體系 (Figure 5)\n"
    r.font.name = FONT_HEADING
    r.font.size = Pt(12.5)
    r.font.bold = True
    r.font.color.rgb = BRAND_SAGE
    
    p_body = tf_cl.add_paragraph()
    p_body.space_before = Pt(8)
    r_b = p_body.add_run()
    r_b.text = "✦ Layer 1: 宣告式權限比對 (Declarative Matching)\n   靜態 Glob 與前綴比對規則（如唯讀目錄、允許讀取白名單），未達模型即秒級放行或阻擋。\n\n✦ Layer 2: 拒絕次數追蹤 (Denial Tracking)\n   後台子代理僅開放 Layer 1~2（避免彈窗卡死）；持續追蹤單會話拒絕次數，超限後自動降級處置。\n\n✦ Layer 3: 互動式人機提示 (Interactive Prompting)\n   高危動作（修改檔案、發送網路請求）向前台使用者彈出審查對話框；子代理遇阻則升級至父級協調器處理。\n\n★ 核心設計：權限狀態每代理隔離，杜絕非同步並行時的跨代理權限污染。"
    r_b.font.name = FONT_BODY
    r_b.font.size = Pt(10)
    r_b.font.color.rgb = TEXT_BODY
    
    # Right Box: Codex 4 Layers + Bwrap Sandboxing
    box_cx = s10.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.833), Inches(1.75), Inches(5.7), Inches(5.2))
    box_cx.fill.solid()
    box_cx.fill.fore_color.rgb = BG_CARD
    box_cx.line.color.rgb = BORDER_CARD
    box_cx.line.width = Pt(1)
    
    tb_cx = s10.shapes.add_textbox(Inches(7.033), Inches(1.9), Inches(5.3), Inches(4.9))
    tf_cx = tb_cx.text_frame
    tf_cx.word_wrap = True
    p = tf_cx.paragraphs[0]
    r = p.add_run()
    r.text = "Codex CLI: 四層防禦棧與原生沙盒隔離\n"
    r.font.name = FONT_HEADING
    r.font.size = Pt(12.5)
    r.font.bold = True
    r.font.color.rgb = BRAND_TERRA
    
    p_body = tf_cx.add_paragraph()
    p_body.space_before = Pt(8)
    r_b = p_body.add_run()
    r_b.text = "✦ Layer 1: Starlark 執行策略 (Policy-as-Code)\n   採用 Starlark 腳本撰寫 prefix_rule 與 network_rule；支援在策略檔內撰寫可執行測試案例。\n\n✦ Layer 2: 生命週期 Hooks\n   吸收 Claude Code 事件詞彙 (PreToolUse, PermissionRequest, PostToolUse)，支援外部阻斷攔截。\n\n✦ Layer 3: Guardian 專屬審批模型\n   在需要時呼叫獨立輕量 Guardian 模型審查潛在惡意行為。\n\n✦ Layer 4: 原生 OS 容器沙盒 (Bubblewrap / Seatbelt)\n   Linux 採用 Bubblewrap 命名空間微隔離 (--ro-bind, --unshare-net, --unshare-pid)，杜絕主機穿透。"
    r_b.font.name = FONT_BODY
    r_b.font.size = Pt(10)
    r_b.font.color.rgb = TEXT_BODY
    
    add_footer(s10, 10)

    # --------------------------------------------------------------------------
    # SLIDE 11: 【重繪論文圖六】六大多代理協同拓撲 (Figure 6 Re-drawn)
    # --------------------------------------------------------------------------
    s11 = prs.slides.add_slide(blank_layout)
    apply_warm_background(s11)
    add_header(s11, "【重繪論文圖六】六大多智慧體協同拓撲全景 (Figure 6)", "拓撲架構", "Figure 6: Multi-Agent Topology Archetypes Across Eleven Production Systems")
    
    topo_w = 3.75
    topo_h = 2.45
    topo_gap_x = 0.24
    topo_gap_y = 0.20
    
    topos = [
        ("1. 單代理獨立迴圈 (Single-agent)", "Mini-SWE-Agent, Aider, Pi", "無派工工具 (No Spawn Tool)，專注單一 Context 反覆迭代，排除多代理複雜性。", BRAND_SAGE),
        ("2. 循序委託 (Sequential)", "Mistral Vibe (task tool)", "父代理啟動單一子代理，父級阻塞等待；子代理回傳摘要後銷毀，單次僅一個活躍。", BRAND_TERRA),
        ("3. 並行子會話 (Parallel Sessions)", "OpenHands, OpenCode", "父代理並行發起多個工作 Session，各自維護獨立歷史記錄，並行執行加速探索。", BRAND_OCHRE),
        ("4. 階層式線程樹 (Thread Tree)", "Codex CLI", "樹狀執行緒結構，支援深度追蹤 (Depth-tracked)、CSV 展開與任務失敗原子化剪枝回滾。", BRAND_SLATE),
        ("5. 遞迴組合 (Recursive)", "Claude Code", "任何 Agent 皆可再遞迴生成子 Agent；跨 Fork 共享 System Prompt 快取，XML 摘要回傳。", BRAND_SAGE),
        ("6. 註冊表與跨行程協議", "Gemini CLI, OpenClaw, Hermes", "透過 Agent 註冊表依名稱調度，跨行程邊界透過 ACP / A2A / SQLite 協同通訊。", BRAND_TERRA)
    ]
    
    for idx, (t_title, t_rep, t_desc, t_color) in enumerate(topos):
        row = idx // 3
        col = idx % 3
        x = 0.8 + col * (topo_w + topo_gap_x)
        y = 1.75 + row * (topo_h + topo_gap_y)
        
        card = s11.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(x), Inches(y), Inches(topo_w), Inches(topo_h))
        card.fill.solid()
        card.fill.fore_color.rgb = BG_CARD
        card.line.color.rgb = BORDER_CARD
        card.line.width = Pt(1)
        
        tb = s11.shapes.add_textbox(Inches(x + 0.15), Inches(y + 0.12), Inches(topo_w - 0.3), Inches(topo_h - 0.24))
        tf = tb.text_frame
        tf.word_wrap = True
        p0 = tf.paragraphs[0]
        r0 = p0.add_run()
        r0.text = t_title + "\n"
        r0.font.name = FONT_HEADING
        r0.font.size = Pt(11)
        r0.font.bold = True
        r0.font.color.rgb = t_color
        
        p_rep = tf.add_paragraph()
        r_rep = p_rep.add_run()
        r_rep.text = f"代表：{t_rep}\n"
        r_rep.font.name = FONT_BODY
        r_rep.font.size = Pt(9.5)
        r_rep.font.bold = True
        r_rep.font.color.rgb = TEXT_HEADLINE
        
        p_desc = tf.add_paragraph()
        p_desc.space_before = Pt(4)
        r_desc = p_desc.add_run()
        r_desc.text = t_desc
        r_desc.font.name = FONT_BODY
        r_desc.font.size = Pt(9.5)
        r_desc.font.color.rgb = TEXT_BODY
        
    add_footer(s11, 11)

    # --------------------------------------------------------------------------
    # SLIDE 12: 【重繪論文圖七】Claude Code 協調者-工兵派工 (Figure 7 Re-drawn)
    # --------------------------------------------------------------------------
    s12 = prs.slides.add_slide(blank_layout)
    apply_warm_background(s12)
    add_header(s12, "【重繪論文圖七】協調者與工兵四階段派工流 (Figure 7)", "派工流模型", "Figure 7: Lead Agent Orchestrating Whitelisted Workers through Structured Phases")
    
    # Top Box: Lead Agent
    lead_box = s12.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.75), Inches(11.733), Inches(1.3))
    lead_box.fill.solid()
    lead_box.fill.fore_color.rgb = RGBColor(0xEA, 0xF0, 0xEC)
    lead_box.line.color.rgb = BRAND_SAGE
    lead_box.line.width = Pt(1.5)
    
    tb_lead = s12.shapes.add_textbox(Inches(1.0), Inches(1.85), Inches(11.333), Inches(1.1))
    tf_lead = tb_lead.text_frame
    tf_lead.word_wrap = True
    p_l = tf_lead.paragraphs[0]
    r_l = p_l.add_run()
    r_l.text = "✦ 主協調代理 (Lead Coordinator) —— 掌握全域專案狀態與階層推進\n"
    r_l.font.name = FONT_HEADING
    r_l.font.size = Pt(12)
    r_l.font.bold = True
    r_l.font.color.rgb = BRAND_SLATE
    r_l_desc = tf_lead.add_paragraph().add_run()
    r_l_desc.text = "負責將複雜需求拆解，依序推進四個不可逆階段；指派具備嚴格工具白名單（16 Tools）之非同步工兵代理，並即時合成回傳之 XML 報告。"
    r_l_desc.font.name = FONT_BODY
    r_l_desc.font.size = Pt(10)
    r_l_desc.font.color.rgb = TEXT_BODY
    
    # Four Stage Boxes
    stage_w = 2.75
    stage_gap = 0.24
    stages = [
        ("階段 1: Research (調研)", "唯讀檢索子代理", ["FileRead, Grep, Glob", "WebSearch, WebFetch", "探索架構並提煉假說", "僅回傳關鍵行號與摘要"], BRAND_SAGE),
        ("階段 2: Synthesis (合成)", "主協調者決策", ["對比調研代理報告", "校驗相依套件與影響面", "確認技術方案與補丁邊界", "排定執行工兵修訂順序"], BRAND_TERRA),
        ("階段 3: Implement (實作)", "受限寫入工兵", ["FileEdit, FileWrite", "Bash, EnterWorktree", "嚴格白名單沙盒執行", "拒絕未授權網路連線"], BRAND_OCHRE),
        ("階段 4: Verification (校驗)", "測試與審查工兵", ["執行測試集驗證", "AST 語法樹靜態分析", "若未通過立即回滾分支", "產出交付報告閉環"], BRAND_SLATE)
    ]
    
    for idx, (s_title, s_sub, s_items, s_color) in enumerate(stages):
        sx = 0.8 + idx * (stage_w + stage_gap)
        scard = s12.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(sx), Inches(3.25), Inches(stage_w), Inches(3.7))
        scard.fill.solid()
        scard.fill.fore_color.rgb = BG_CARD
        scard.line.color.rgb = BORDER_CARD
        scard.line.width = Pt(1)
        
        tb_s = s12.shapes.add_textbox(Inches(sx + 0.15), Inches(3.4), Inches(stage_w - 0.3), Inches(3.4))
        tf_s = tb_s.text_frame
        tf_s.word_wrap = True
        
        p = tf_s.paragraphs[0]
        r = p.add_run()
        r.text = s_title + "\n"
        r.font.name = FONT_HEADING
        r.font.size = Pt(11)
        r.font.bold = True
        r.font.color.rgb = s_color
        
        p_sub = tf_s.add_paragraph()
        r_sub = p_sub.add_run()
        r_sub.text = s_sub + "\n"
        r_sub.font.name = FONT_BODY
        r_sub.font.size = Pt(9.5)
        r_sub.font.bold = True
        r_sub.font.color.rgb = TEXT_HEADLINE
        
        for item in s_items:
            p_it = tf_s.add_paragraph()
            p_it.space_before = Pt(4)
            r_it = p_it.add_run()
            r_it.text = f"• {item}"
            r_it.font.name = FONT_BODY
            r_it.font.size = Pt(9.5)
            r_it.font.color.rgb = TEXT_BODY
            
    add_footer(s12, 12)

    # --------------------------------------------------------------------------
    # SLIDE 13: D7 擴展機制：MCP 與 SKILL.md 雙雄並立
    # --------------------------------------------------------------------------
    s13 = prs.slides.add_slide(blank_layout)
    apply_warm_background(s13)
    add_header(s13, "D7 擴展機制：MCP 連網協議與 SKILL.md 知識封裝", "子系統深度", "系統互聯協議與智慧體領域微程式碼 (Bytecode) 的分工協同")
    
    add_enlarged_bullet_card(
        s13, left=0.8, top=1.75, width=5.7, height=4.2,
        title="1. MCP (Model Context Protocol) 協議",
        items=[
            "8/11 系統全面支援：迅速確立為 AI 代理與外部 API、資料庫與內部服務通訊之標準 RPC 規範。",
            "Client / Server 鬆散耦合：Harness 作為 Client，外部工具封裝為獨立行程，實現架構安全解耦。",
            "跨語言與跨平台：支援 stdio 與 SSE/HTTP 傳輸，抹平 Python、TypeScript、Rust 語言壁壘。",
            "權限安全微隔離：外部外掛在獨立行程執行，杜絕惡意外掛直接污染或注入 Harness 核心記憶體。"
        ],
        tag="CONNECTIVITY",
        accent_color=BRAND_SAGE
    )
    add_enlarged_bullet_card(
        s13, left=6.833, top=1.75, width=5.7, height=4.2,
        title="2. SKILL.md 領域知識規範標準",
        items=[
            "9/11 系統原生支援：成為智慧體軟體工程最普及之標準領域知識微程式碼 (Bytecode)。",
            "Markdown + YAML 宣告：輕量易維護，包含 name, description, paths, requires 等清晰元資料。",
            "遞延加載機制 (Deferred Loading)：平時僅在 Prompt 注入簡短索引，任務匹配時才動態掛載全文。",
            "節省高達 90% Context：徹底根絕過去將所有 SOP 規章全部硬塞入 System Prompt 的 Token 浪費。"
        ],
        tag="KNOWLEDGE STANDARD",
        accent_color=BRAND_TERRA
    )
    add_centered_quote_card(
        s13, left=0.8, top=6.05, width=11.733, height=0.9,
        en_quote="MCP defines how agents connect to tools; SKILL.md defines how agents acquire specialized wisdom.",
        highlight_word="SKILL.md defines how agents acquire specialized wisdom",
        zh_quote="MCP 定義了智慧體如何連結工具；而 SKILL.md 則定義了智慧體如何精準獲取專業領域智慧。"
    )
    add_footer(s13, 13)

    # --------------------------------------------------------------------------
    # SLIDE 14: 缺席一：100% 拋棄通用代理框架 (Observation 13.2)
    # --------------------------------------------------------------------------
    s14 = prs.slides.add_slide(blank_layout)
    apply_warm_background(s14)
    add_header(s14, "缺席之一：100% 拋棄通用代理框架 (No General Frameworks)", "核心實證震撼", "11 款一線生產系統零採用 LangChain / AutoGen / CrewAI 的深層架構反思")
    
    add_enlarged_bullet_card(
        s14, left=0.8, top=1.75, width=5.7, height=5.2,
        title="1. 實證調查結果 (Empirical Finding)",
        items=[
            "零採用率客觀事實：審查 11 款頂尖系統依賴清單，100% 無 LangChain、CrewAI、AutoGen 或 Semantic Kernel。",
            "連原廠都跳過自家框架：Google Gemini CLI 甚至完全不使用 Google 官方的 Genkit 或 ADK 框架。",
            "全員採用原生迴圈：全數基於語言原生之非同步事件迴圈 (Async/Await While Loop) 手工打造。",
            "教學展示與工業級產品反差：展示專案熱衷通用框架，但高負載工業級產品全數避而遠之。"
        ],
        tag="SHOCKING FACT",
        accent_color=BRAND_TERRA
    )
    add_enlarged_bullet_card(
        s14, left=6.833, top=1.75, width=5.7, height=5.2,
        title="2. 四大工程淘汰主因剖析 (Root Causes)",
        items=[
            "抽象洩漏嚴重 (Leaky Abstractions)：通用框架試圖相容客服、聊天等多場景，抽象過於臃腫且無法精確調控。",
            "微秒級控制權喪失：編程任務仰賴事件暫停、手動編輯歷史、動態抽換工具集，框架黑盒子造成致命阻礙。",
            "Prompt Caching 遭破壞：通用框架不可見的提示詞拼接邏輯頻繁破壞原廠 KV 快取邊界，延遲費用暴增數倍。",
            "除錯維護成本高昂：框架層層包裝使 Exception 堆疊極度深奧，無法進行生產級錯誤診斷與自動修復。"
        ],
        tag="ARCHITECTURAL LESSON",
        accent_color=BRAND_SAGE
    )
    add_footer(s14, 14)

    # --------------------------------------------------------------------------
    # SLIDE 15: 缺席二：全面拋棄向量代碼檢索 (Observation 13.2)
    # --------------------------------------------------------------------------
    s15 = prs.slides.add_slide(blank_layout)
    apply_warm_background(s15)
    add_header(s15, "缺席之二：全面拋棄向量代碼檢索 (No Vector Code RAG)", "核心實證震撼", "代碼語義高度結構化，ripgrep 與 tree-sitter 確定性武器庫的降維打擊")
    
    add_enlarged_bullet_card(
        s15, left=0.8, top=1.75, width=5.7, height=5.2,
        title="1. 向量代碼檢索 (Code RAG) 的失效本質",
        items=[
            "語意模糊 vs 語法確定性：向量擅長自然語言概念比對，但面對函式簽名、介面實作等確定性符號時精度極低。",
            "語境切割破碎化：將程式碼依 Chunk 暴力切分，徹底割裂了 AST 語法樹階層與跨檔案繼承關係。",
            "高雜訊誘發幻覺：相似度回傳常帶有同名過時函式，極易誤導模型寫出錯誤的調用參數與型別。",
            "索引重建開銷巨大：大型專案每次 Git 切換分支或 Commit，重新計算向量 Embeddings 既慢又耗費算力。"
        ],
        tag="WHY VECTOR FAILS",
        accent_color=BRAND_TERRA
    )
    add_enlarged_bullet_card(
        s15, left=6.833, top=1.75, width=5.7, height=5.2,
        title="2. 一線 Harness 的確定性檢索武器庫",
        items=[
            "ripgrep (全域正則搜尋)：毫秒級遍歷數百萬行代碼，精確定位變數、路由與錯誤碼定義行號。",
            "tree-sitter (AST 結構解析)：跨語言語法樹解析，精準提取 Class、Method 與跨模組依賴鏈。",
            "ctags / 符號索引圖譜：輕量化建立全域符號表，支持快速跳轉至定義點與參考點。",
            "Markdown 規格導航：由專案架構文件引導，結合模型的「假說驗證」主動探索，命中率達 98%。"
        ],
        tag="DETERMINISTIC SUITE",
        accent_color=BRAND_SAGE
    )
    add_footer(s15, 15)

    # --------------------------------------------------------------------------
    # SLIDE 16: 平台化轉型論題 (The Platform Turn)
    # --------------------------------------------------------------------------
    s16 = prs.slides.add_slide(blank_layout)
    apply_warm_background(s16)
    add_header(s16, "平台化轉型論題：從單機 CLI 走向 AI 運行時作業系統", "產業趨勢", "Coding Harness 完成由單純開發者輔助腳本向企業級 AI-ROS 的歷史性跨越")
    
    add_enlarged_bullet_card(
        s16, left=0.8, top=1.75, width=5.7, height=5.2,
        title="1. 平台化轉型三大特徵 (The Platform Turn)",
        items=[
            "AI 運行時操作系統確立：Harness 已進化為全面掌控執行緒排程、權限沙盒、持久記憶與外掛的底座。",
            "跨陣營組件規範趨同：Codex 採納 Claude Code 的 Hook 命名；OpenHands 原生支援 Claude Code 外掛。",
            "政策由 Prompt 遷移至強型別配置：安全規範與權限全面由自然語言 Prompt 脫離，轉為 Starlark / JSON 治理。",
            "生態標準確立：SKILL.md 與 MCP 成為跨廠商、跨模型共同遵守的事實標準。"
        ],
        tag="PLATFORM ERA",
        accent_color=BRAND_SAGE
    )
    add_enlarged_bullet_card(
        s16, left=6.833, top=1.75, width=5.7, height=5.2,
        title="2. Databricks Omnigent 元框架架構啟示",
        items=[
            "Meta-Harness 的崛起：企業不再單一押注某家原廠，而是在外層建構統一管控網關。",
            "統一 API 同步調度 11 款原廠 Harness：依據任務複雜度動態路由至 Claude Code、Codex 或 Aider。",
            "集中化企業治理：統一收集所有 Harness 的 Token 消耗軌跡、合規日誌與安全性審查報告。",
            "客觀自動化基準評測：以同一套標準基準自動評估不同 Harness 在私有代碼庫上的修復表現，消除廠商宣傳迷思。"
        ],
        tag="META-HARNESS",
        accent_color=BRAND_TERRA
    )
    add_footer(s16, 16)

    # --------------------------------------------------------------------------
    # SLIDE 17: 90 天演化對比表 (Table 15: Longitudinal Diff)
    # --------------------------------------------------------------------------
    s17 = prs.slides.add_slide(blank_layout)
    apply_warm_background(s17)
    add_header(s17, "90 天演化追蹤與收斂趨勢 (Longitudinal Diff Analysis)", "技術演進", "跨季原始碼對比：Hook 生命週期、外掛相容與微核心反動")
    
    headers_s17 = ["演化維度", "90 天前狀態 (Early 2026)", "90 天後最新收斂 (Mid-Late 2026)", "架構工程意義"]
    rows_s17 = [
        ["擴展協議", "各家私有外掛 API，相互隔離", "MCP (8/11) 與 SKILL.md (9/11) 雙標準確立", "生態互通，外掛開發者擺脫重複造輪子"],
        ["安全防禦", "提示詞宣告 (Prompt Guardrails)", "Starlark 腳本 + 容器沙盒 + 外部守護模型", "杜絕 Prompt Injection，達到企業生產級安全標準"],
        ["代碼編輯", "整檔寫入 (Whole-file) 仍佔多數", "Search-and-Replace + 模糊比對瀑布全面普及", "補丁成功率從 70% 提升至 95%，Token 消耗減半"],
        ["生命週期", "簡單 While-Loop，無中斷點", "標準化 Hook 系統 (pre-tool, post-tool, on-error)", "支援動態權限審查、日誌插樁與即時人工介入"],
        ["系統複雜度", "不斷疊加功能，架構持續膨脹", "出現 Pi 等微核心極簡主義反動", "驗證核心簡潔性在長期除錯與維護上的巨大優勢"],
        ["多模型策略", "壁壘分明，原廠鎖定嚴重", "Omnigent 等元框架興起，底層原廠可抽換", "企業級採購轉向多模型混合調度與彈性容災"]
    ]
    col_w_s17 = [1.8, 3.2, 3.8, 2.933]
    create_enlarged_table(s17, left=0.8, top=1.75, width=11.733, height=5.2, headers=headers_s17, rows_data=rows_s17, col_widths=col_w_s17, font_size=8.5)
    add_footer(s17, 17)

    # --------------------------------------------------------------------------
    # SLIDE 18: 18 條架構實踐指南 (Recommendations 1~9)
    # --------------------------------------------------------------------------
    s18 = prs.slides.add_slide(blank_layout)
    apply_warm_background(s18)
    add_header(s18, "實踐者軍規 (上)：第 1 至第 9 條架構設計實踐指南", "實踐軍規", "論文 Section 16 精煉：涵蓋迴圈、模型、工具、編輯、記憶與安全防護")
    
    col3_w = 3.75
    add_enlarged_bullet_card(
        s18, left=0.8, top=1.75, width=col3_w, height=5.2,
        title="1. 迴圈與模型整合 (Rec 1-3)",
        items=[
            "Rec 1: 始於線性迴圈，待出現多個獨立輪次策略再演進為中間件管線。",
            "Rec 2: 自有基底模型者深度耦合原廠並保留 Fallback；多模型者維持單一集中適配層。",
            "Rec 3: 始於單一 Bash 工具，僅在觀察到具體失敗模式時再增設微工具。"
        ],
        tag="LOOP & MODEL",
        accent_color=BRAND_SAGE
    )
    add_enlarged_bullet_card(
        s18, left=0.8 + col3_w + col3_gap, top=1.75, width=col3_w, height=5.2,
        title="2. 工具、編輯與記憶 (Rec 4-6)",
        items=[
            "Rec 4: 工具數量超過 15 個時，必須導入遞延工具加載 (Deferred Loading)。",
            "Rec 5: 根據模型等級匹配編輯合約：頂級模型採精確子字串替換，中弱模型採模糊寬容瀑布。",
            "Rec 6: 自動探索專案層級 Markdown 規格文件 (AGENTS.md, CLAUDE.md) 並相容鄰居命名。"
        ],
        tag="TOOLS & MEMORY",
        accent_color=BRAND_TERRA
    )
    add_enlarged_bullet_card(
        s18, left=0.8 + (col3_w + col3_gap)*2, top=1.75, width=col3_w, height=5.2,
        title="3. 壓縮、檢索與安全 (Rec 7-9)",
        items=[
            "Rec 7: 實作閾值邊界壓縮，保留最近完整推導尾端，增量合併摘要並相容溢位復原。",
            "Rec 8: 嚴禁對程式碼建構向量 RAG，全面改採 ripgrep、tree-sitter 與目錄走訪。",
            "Rec 9: 開發者半信任場景實作三模式審批 (PLAN / DEFAULT / YOLO) 與權限作用域。"
        ],
        tag="SECURITY & RAG",
        accent_color=BRAND_OCHRE
    )
    add_footer(s18, 18)

    # --------------------------------------------------------------------------
    # SLIDE 19: 18 條架構實踐指南 (Recommendations 10~18 & Anti-Patterns)
    # --------------------------------------------------------------------------
    s19 = prs.slides.add_slide(blank_layout)
    apply_warm_background(s19)
    add_header(s19, "實踐者軍規 (下)：第 10 至第 18 條架構指南與反模式", "實踐軍規", "論文 Section 16 精煉：涵蓋沙盒、多代理、擴展標準與四大嚴格反模式")
    
    add_enlarged_bullet_card(
        s19, left=0.8, top=1.75, width=col3_w, height=5.2,
        title="4. 沙盒與多代理 (Rec 10-13)",
        items=[
            "Rec 10: 企業自動化場景實作作業系統級沙盒 (Bubblewrap/Seatbelt) 與 Policy-as-Code。",
            "Rec 11: 安全規則務必採用資料結構或專用策略檔撰寫，嚴禁散落於提示詞散文。",
            "Rec 12: 保持單代理架構，直到平行 Context 隔離帶來的收益明確大於序列搜尋。",
            "Rec 13: 釋出 ACP 伺服器以相容 IDE 與外部元協調器，主從內部協同保持行程內。"
        ],
        tag="SANDBOX & MULTI-AGENT",
        accent_color=BRAND_SAGE
    )
    add_enlarged_bullet_card(
        s19, left=0.8 + col3_w + col3_gap, top=1.75, width=col3_w, height=5.2,
        title="5. 擴展標準 (Rec 14)",
        items=[
            "Rec 14 優先級：以 SKILL.md 封裝能力範本與領域 SOP，以 MCP 整合外部程序與 API。",
            "技能遞延加載：平時僅暴露清單索引，命中任務動態載入完整規格，省 90% 提示詞空間。",
            "第三方技能套件治理：將第三方 Skill 視為依賴套件，建立信任階層、掃描與隔離機制。"
        ],
        tag="SKILLS & MCP",
        accent_color=BRAND_TERRA
    )
    add_enlarged_bullet_card(
        s19, left=0.8 + (col3_w + col3_gap)*2, top=1.75, width=col3_w, height=5.2,
        title="6. 四大嚴格反模式 (Rec 15-18)",
        items=[
            "Rec 15 禁令：嚴禁用 LangChain/AutoGen 等通用框架做 Runtime，改採原生迴圈或 Harness SDK。",
            "Rec 16 禁令：嚴禁為程式碼建立向量 Embeddings 檢索層，優先證明其優於 ripgrep。",
            "Rec 17 禁令：嚴禁將上游 SaaS API 1:1 包裝為肥大工具，應予以精煉整併。",
            "Rec 18 警戒：勿過度設計卡死偵測，但務必配置十幾行代碼的廉價計數上限保險。"
        ],
        tag="ANTI-PATTERNS",
        accent_color=BRAND_OCHRE
    )
    add_footer(s19, 19)

    # --------------------------------------------------------------------------
    # SLIDE 20: 產業落地見解與企業導入戰略
    # --------------------------------------------------------------------------
    s20 = prs.slides.add_slide(blank_layout)
    apply_warm_background(s20)
    add_header(s20, "研析見解與產業落地指導：打造企業級高可靠 Harness", "實踐戰略", "告別玩具級原型，以確定性工程、沙盒治理與標準化技能構建長期競爭壁壘")
    
    col4_w = 2.75
    gap4_x = 0.24
    
    add_enlarged_bullet_card(
        s20, left=0.8, top=1.75, width=col4_w, height=5.2,
        title="1. 預算重配置戰略",
        items=[
            "打破模型至上偏誤：切勿將 90% 預算押注於天價模型 API。",
            "加碼投資 Harness 架構：強韌的 Harness 能讓普通模型超越脆弱架構下的頂級模型。",
            "掌控長程推理成本：藉助 Prompt Caching 與微修剪，降低長程任務 60% 開銷。"
        ],
        tag="BUDGET",
        accent_color=BRAND_SAGE
    )
    add_enlarged_bullet_card(
        s20, left=0.8 + col4_w + gap4_x, top=1.75, width=col4_w, height=5.2,
        title="2. 堅決揚棄玩具架構",
        items=[
            "拒絕大而無當的通用框架：生產系統嚴禁引進肥大黑盒庫。",
            "回歸 Unix 哲學：堅持手寫非同步迴圈，保持微秒級事件控制權與清晰除錯軌跡。",
            "以 Git 為原生底座：將版本控制作為狀態復原與差異比較的天然基準點。"
        ],
        tag="RUNTIME",
        accent_color=BRAND_TERRA
    )
    add_enlarged_bullet_card(
        s20, left=0.8 + (col4_w + gap4_x)*2, top=1.75, width=col4_w, height=5.2,
        title="3. 擁抱確定性檢索",
        items=[
            "停止盲目建構代碼向量庫：全面換裝 ripgrep、tree-sitter 與語法符號索引。",
            "善用結構化 Markdown：為核心系統維護精確架構導航規格。",
            "主動探索閉環：讓模型提出假說並透過精準搜尋驗證，精度完勝向量 RAG。"
        ],
        tag="DETERMINISTIC",
        accent_color=BRAND_OCHRE
    )
    add_enlarged_bullet_card(
        s20, left=0.8 + (col4_w + gap4_x)*3, top=1.75, width=col4_w, height=5.2,
        title="4. 組織級資產沉澱",
        items=[
            "推動 SKILL.md 標準化：將企業內部最佳工程實踐、審查規則模組化封裝。",
            "導入遞延加載機制：徹底杜絕 System Prompt 肥大化與注意力稀釋。",
            "建立沙盒防護線：在研發環境預設容器隔離與人機協同審批。"
        ],
        tag="ORGANIZATION",
        accent_color=BRAND_SLATE
    )
    add_footer(s20, 20)

    # --------------------------------------------------------------------------
    # SLIDE 21: 關鍵術語與英文縮寫對照表 (Glossary)
    # --------------------------------------------------------------------------
    s21 = prs.slides.add_slide(blank_layout)
    apply_warm_background(s21)
    add_header(s21, "附錄一：關鍵術語解析與英文縮寫對照表 (Glossary)", "名詞對照", "精選論文中跨 11 款系統頻繁出現之核心架構術語與標準定義")
    
    headers_s21 = ["術語 / 縮寫", "英文全稱", "技術意涵與在 Harness 中的核心角色"]
    rows_s21 = [
        ["Harness", "Execution Harness / Runtime", "包覆底層模型的主動執行環境，負責事件循環、工具排程、沙盒隔離與生命週期管理"],
        ["MCP", "Model Context Protocol", "由 Anthropic 推動並成為產業共識的開放 RPC 協議，用於連通外部工具、API 與資料庫"],
        ["SKILL.md", "Agent Skill Specification", "智慧體標準領域知識封裝規範，採 Markdown+YAML 格式，支援遞延動態加載以節省 Context"],
        ["ACP", "Agent Client Protocol", "用於 IDE 與 Agent 主機連線的標準通訊協議 (Zed, JetBrains, OpenHands, Omnigent 均支援)"],
        ["Stuck Detector", "Infinite Loop / Oscillation Detector", "死循環與震盪偵測器，監控同指令反覆失敗或工具呼叫空轉，並主動介入中斷修復"],
        ["Compaction", "Context Compaction / Micro-pruning", "上下文壓縮與微修剪管線，非破壞性移除過時終端日誌與折疊工具呼叫，保持訊號純淨"],
        ["HITL", "Human-In-The-Loop", "人機協同審批機制，針對刪檔、代碼發布等高危關鍵行為強制暫停並要求人工簽核授權"],
        ["AST", "Abstract Syntax Tree", "抽象語法樹，用於高確定性代碼結構解析 (如 tree-sitter)，完勝傳統向量相似度檢索"],
        ["Meta-Harness", "Meta-Orchestration Runtime", "如 Databricks Omnigent，在多款原廠 Harness 之上建立的跨廠商統一治理、評測與調度層"]
    ]
    col_w_s21 = [2.0, 3.2, 6.533]
    create_enlarged_table(s21, left=0.8, top=1.75, width=11.733, height=5.2, headers=headers_s21, rows_data=rows_s21, col_widths=col_w_s21, font_size=8.5)
    add_footer(s21, 21)

    # --------------------------------------------------------------------------
    # SLIDE 22: 資料來源與學術文獻溯源 (References & Sources)
    # --------------------------------------------------------------------------
    s22 = prs.slides.add_slide(blank_layout)
    apply_warm_background(s22)
    add_header(s22, "附錄二：文獻出處、論文版本與研究方法論 (References)", "文獻溯源", "詳細標記學術論文官方出處、審查系統版本 Commit 與分析方法論")
    
    headers_s22 = ["類別", "項目名稱", "文獻出處 / 系統版本 Commit / 官方標註"]
    rows_s22 = [
        ["學術母篇", "arXiv:2609.00006v1", "Harness Engineering: Anatomy, Architecture, and Evolution of Coding Agents (Sept 2026)"],
        ["研究機構", "Wavestone AI Lab", "Paul Barbaste, Tristan Darrigol, Germain Vu, Tom Wiltberger (巴黎/紐約實驗室)"],
        ["原廠旗艦", "Claude Code & Codex", "Anthropic @anthropic-ai/claude-code (TS) · OpenAI Codex CLI (Rust In-Tree Bubblewrap)"],
        ["開源代表", "OpenHands & Aider", "All-Hands-AI/OpenHands (Event-Sourced V1) · Paul-Gauthier/aider (Git Native Diff)"],
        ["極簡代表", "Mini-SWE-Agent & Pi", "SWE-bench/mini-swe-agent (100 lines) · Mario Zechner/pi (Micro-kernel architecture)"],
        ["元框架對比", "Databricks Omnigent", "Omnigent: A Meta-Harness Orchestrating Eleven Vendor Frameworks Behind a Unified API"],
        ["研究方法論", "跨系統靜態與動態審查", "全文 4,170 行原始碼解構、47 項特徵矩陣量化、90 天時間差分 (April vs July 2026 Snapshots)"]
    ]
    col_w_s22 = [1.8, 2.5, 7.433]
    create_enlarged_table(s22, left=0.8, top=1.75, width=11.733, height=4.2, headers=headers_s22, rows_data=rows_s22, col_widths=col_w_s22, font_size=8.5)
    
    ref_card = s22.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(6.08), Inches(11.733), Inches(0.92))
    ref_card.fill.solid()
    ref_card.fill.fore_color.rgb = BG_CARD
    ref_card.line.color.rgb = BORDER_CARD
    ref_card.line.width = Pt(1)
    
    tb_ref = s22.shapes.add_textbox(Inches(1.0), Inches(6.12), Inches(11.333), Inches(0.8))
    tf_ref = tb_ref.text_frame
    tf_ref.word_wrap = True
    tf_ref.margin_left = tf_ref.margin_top = tf_ref.margin_right = tf_ref.margin_bottom = 0
    p_r0 = tf_ref.paragraphs[0]
    r_r0 = p_r0.add_run()
    r_r0.text = "✦ 研析方法與格式遵循宣告："
    r_r0.font.name = FONT_HEADING
    r_r0.font.size = Pt(9.5)
    r_r0.font.bold = True
    r_r0.font.color.rgb = BRAND_SAGE
    
    p_r1 = tf_ref.add_paragraph()
    r_r1 = p_r1.add_run()
    r_r1.text = "本簡報本於學術論文全文實證研究，徹底重繪圖一（D1-D7 架構）、圖二（迴圈範式）、圖四（記憶策略）、圖五（安全防禦棧）、圖六（多代理拓撲）、圖七（派工流程），並融入跨季對比表與 18 條架構軍規。全面套用「pptx 樣板一」規範生成。"
    r_r1.font.name = FONT_BODY
    r_r1.font.size = Pt(8.5)
    r_r1.font.color.rgb = TEXT_MUTED
    
    add_footer(s22, 22)
    
    out_dir = r"d:\JavaDO\執行框架"
    out_name = "Harness Engineering 論文解析.pptx"
    out_path = os.path.join(out_dir, out_name)
    prs.save(out_path)
    print(f"Successfully generated 22 slides to: {out_path}")

if __name__ == "__main__":
    build_all_slides()
