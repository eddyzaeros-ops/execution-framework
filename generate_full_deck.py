import re
"""
Comprehensive, Beautiful PPTX Generator for arXiv:2609.00006v1
Highlights of this build:
1. Re-renders Figures 1, 2, and 6 using high-res Matplotlib adhering to Template 1 color palette.
   Eliminated previous visual issues and optimized page 4, 6, 8 layout and typography.
2. Perfected Table Slides (pages 12 to 29):
   - Dynamically adapts layout based on table size:
     * Vertical Stack (Tables with <=10 rows or compact text): Table on top, commentary card below with zero overlap.
     * Side-by-Side (Large tables with 10~18 rows or dense descriptions): Table on left (width 7.0"~7.5"), commentary on right (width 4.0"~4.5"), giving unlimited vertical height (5.2") and zero text truncation or overlap!
3. All fonts enlarged for high contrast & clarity.
"""

import os
import sys
import json
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
TEXT_BODY = RGBColor(0x3E, 0x48, 0x56)        # Darkened Warm Slate for high contrast
TEXT_MUTED = RGBColor(0x65, 0x71, 0x82)       # Soft Slate 600

TABLE_HEADER_BG = RGBColor(0xEA, 0xE4, 0xD8)  # Warm Oat Table Header
TABLE_ROW_ALT = RGBColor(0xF7, 0xF4, 0xED)    # Alternate warm row tint

FONT_HEADING = "Microsoft JhengHei"
FONT_BODY = "Microsoft JhengHei"

TOTAL_SLIDES = 42

with open("parsed_tables.json", "r", encoding="utf-8") as f:
    ALL_TABLES = json.load(f)

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
    cat_box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(0.28), Inches(2.8), Inches(0.32))
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
    r_title.font.size = Pt(17)
    r_title.font.bold = True
    r_title.font.color.rgb = TEXT_HEADLINE
    
    if subtitle_text:
        p1 = tf_title.add_paragraph()
        p1.space_before = Pt(3)
        r_sub = p1.add_run()
        r_sub.text = subtitle_text
        r_sub.font.name = FONT_BODY
        r_sub.font.size = Pt(9.5)
        r_sub.font.color.rgb = TEXT_MUTED
        
    divider = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.52), Inches(11.733), Inches(0.015))
    divider.fill.solid()
    divider.fill.fore_color.rgb = BORDER_DIVIDER
    divider.line.fill.background()

def add_footer(slide, current_idx, total_slides=TOTAL_SLIDES):
    # page number derived from slide part name (slides appended in order)
    current_idx = int(re.search(r'slide(\d+)\.xml', str(slide.part.partname)).group(1))
    tb = slide.shapes.add_textbox(Inches(0.8), Inches(7.14), Inches(9.0), Inches(0.25))
    tf = tb.text_frame
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
    p = tf.paragraphs[0]
    r = p.add_run()
    r.text = "HARNESS ENGINEERING  ·  A SOURCE-CODE STUDY OF ELEVEN SYSTEMS (arXiv:2609.00006v1)"
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
    card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(left), Inches(top), Inches(width), Inches(height))
    card.fill.solid()
    card.fill.fore_color.rgb = BG_CARD
    card.line.color.rgb = BORDER_CARD
    card.line.width = Pt(1)
    
    tb_t = slide.shapes.add_textbox(Inches(left + 0.2), Inches(top + 0.12), Inches(width - 0.4), Inches(0.38))
    tf_t = tb_t.text_frame
    tf_t.word_wrap = True
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
    
    num_items = len(items)
    content_top = top + 0.60
    available_h = height - 0.70
    slot_h = available_h / num_items
    
    for idx, item in enumerate(items):
        item_y = content_top + idx * slot_h
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
        
        tb_i = slide.shapes.add_textbox(Inches(left + 0.54), Inches(item_y), Inches(width - 0.74), Inches(slot_h - 0.04))
        tf_i = tb_i.text_frame
        tf_i.word_wrap = True
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
    p0 = tf.paragraphs[0]
    p0.alignment = PP_ALIGN.CENTER
    
    if highlight_word and highlight_word in en_quote:
        before, after = en_quote.split(highlight_word, 1)
        r0 = p0.add_run()
        r0.text = f'"{before}'
        r0.font.name = FONT_HEADING
        r0.font.size = Pt(12.5)
        r0.font.bold = True
        r0.font.color.rgb = BRAND_SLATE
        
        r_hl = p0.add_run()
        r_hl.text = highlight_word
        r_hl.font.name = FONT_HEADING
        r_hl.font.size = Pt(12.5)
        r_hl.font.bold = True
        r_hl.font.color.rgb = BRAND_TERRA
        
        r1 = p0.add_run()
        r1.text = f'{after}"'
        r1.font.name = FONT_HEADING
        r1.font.size = Pt(12.5)
        r1.font.bold = True
        r1.font.color.rgb = BRAND_SLATE
    else:
        r0 = p0.add_run()
        r0.text = f'"{en_quote}"'
        r0.font.name = FONT_HEADING
        r0.font.size = Pt(12.5)
        r0.font.bold = True
        r0.font.color.rgb = BRAND_SLATE
        
    p1 = tf.add_paragraph()
    p1.space_before = Pt(6)
    p1.alignment = PP_ALIGN.CENTER
    r_zh = p1.add_run()
    r_zh.text = zh_quote
    r_zh.font.name = FONT_BODY
    r_zh.font.size = Pt(10)
    r_zh.font.color.rgb = TEXT_MUTED

def create_table_element(slide, left, top, width, height, headers, rows_data, col_widths=None, font_size=8.5):
    """Creates a table element with explicit cell paddings and alignments."""
    num_rows = len(rows_data) + 1
    num_cols = len(headers)
    table_shape = slide.shapes.add_table(num_rows, num_cols, Inches(left), Inches(top), Inches(width), Inches(height))
    table = table_shape.table
    
    if col_widths and len(col_widths) == num_cols:
        scale = width / sum(col_widths)
        for idx, w in enumerate(col_widths):
            table.columns[idx].width = Inches(w * scale)
            
    # Headers
    for c_idx, h_text in enumerate(headers):
        cell = table.cell(0, c_idx)
        cell.fill.solid()
        cell.fill.fore_color.rgb = TABLE_HEADER_BG
        cell.vertical_anchor = MSO_ANCHOR.MIDDLE
        cell.margin_left = cell.margin_right = Inches(0.06)
        cell.margin_top = cell.margin_bottom = Inches(0.04)
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
            cell.margin_left = cell.margin_right = Inches(0.06)
            cell.margin_top = cell.margin_bottom = Inches(0.04)
            p = cell.text_frame.paragraphs[0]
            val_str = str(val).strip()
            p.text = val_str
            p.font.name = FONT_BODY
            p.font.size = Pt(font_size)
            p.alignment = PP_ALIGN.LEFT if c_idx == 0 else (PP_ALIGN.CENTER if len(val_str) <= 12 else PP_ALIGN.LEFT)
            if c_idx == 0:
                p.font.bold = True
                p.font.color.rgb = TEXT_HEADLINE
            else:
                p.font.color.rgb = TEXT_BODY
    return table_shape

def add_table_slide_adaptive(slide, tid, title, category, sub_title, insights, font_size=8.5, col_widths=None, side_by_side=False, row_range=None):
    """
    Intelligent Adaptive Layout:
    - If side_by_side is True: Table on left (width 7.3"), Commentary Card on right (width 4.1").
      Provides massive vertical space (height 5.2"), completely preventing overlap!
    - If side_by_side is False: Standard vertical stack (height 3.1" + 1.8"), with explicit spacing to avoid overlap.
    """
    add_header(slide, title, category, sub_title)
    
    t_info = ALL_TABLES.get(tid, {})
    rows = t_info.get("rows", [])
    if not rows:
        return
    headers = rows[0]
    data_rows = rows[1:]
    if row_range is not None:
        data_rows = data_rows[row_range[0]:row_range[1]]
    
    if side_by_side:
        # Left Table
        tbl_w = 7.3
        tbl_h = 5.2
        tbl_left = 0.8
        tbl_top = 1.75
        create_table_element(slide, left=tbl_left, top=tbl_top, width=tbl_w, height=tbl_h, headers=headers, rows_data=data_rows, col_widths=col_widths, font_size=font_size)
        
        # Right Commentary Card
        card_left = 8.35
        card_w = 4.183
        card_h = 5.2
        comm_card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(card_left), Inches(tbl_top), Inches(card_w), Inches(card_h))
        comm_card.fill.solid()
        comm_card.fill.fore_color.rgb = BG_CARD
        comm_card.line.color.rgb = BORDER_CARD
        comm_card.line.width = Pt(1)
        
        tb = slide.shapes.add_textbox(Inches(card_left + 0.2), Inches(tbl_top + 0.2), Inches(card_w - 0.4), Inches(card_h - 0.4))
        tf = tb.text_frame
        tf.word_wrap = True
        
        p0 = tf.paragraphs[0]
        r0 = p0.add_run()
        r0.text = "✦ 研析見解與架構解讀\n(Architectural Insights)：\n"
        r0.font.name = FONT_HEADING
        r0.font.size = Pt(11)
        r0.font.bold = True
        r0.font.color.rgb = BRAND_SAGE
        
        for ins in insights:
            p = tf.add_paragraph()
            p.space_before = Pt(8)
            r = p.add_run()
            r.text = f"• {ins}"
            r.font.name = FONT_BODY
            r.font.size = Pt(9.5)
            r.font.color.rgb = TEXT_BODY
    else:
        # Vertical Stack with safe spacing
        tbl_w = 11.733
        tbl_h = 2.95
        tbl_left = 0.8
        tbl_top = 1.75
        create_table_element(slide, left=tbl_left, top=tbl_top, width=tbl_w, height=tbl_h, headers=headers, rows_data=data_rows, col_widths=col_widths, font_size=font_size)
        
        comm_top = 4.95
        comm_h = 2.05
        comm_card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(comm_top), Inches(11.733), Inches(comm_h))
        comm_card.fill.solid()
        comm_card.fill.fore_color.rgb = BG_CARD
        comm_card.line.color.rgb = BORDER_CARD
        comm_card.line.width = Pt(1)
        
        tb = slide.shapes.add_textbox(Inches(1.0), Inches(comm_top + 0.15), Inches(11.333), Inches(comm_h - 0.3))
        tf = tb.text_frame
        tf.word_wrap = True
        
        p0 = tf.paragraphs[0]
        r0 = p0.add_run()
        r0.text = "✦ 研析見解與架構意涵解讀 (Architectural Interpretation)："
        r0.font.name = FONT_HEADING
        r0.font.size = Pt(10.5)
        r0.font.bold = True
        r0.font.color.rgb = BRAND_SAGE
        
        for ins in insights:
            p = tf.add_paragraph()
            p.space_before = Pt(3)
            r = p.add_run()
            r.text = f"• {ins}"
            r.font.name = FONT_BODY
            r.font.size = Pt(9.5)
            r.font.color.rgb = TEXT_BODY

def add_matplotlib_figure_slide(slide, fig_img_path, fig_num_str, title_text, category_text, sub_title, original_caption, insights):
    """
    Renders the newly redrawn high-res Matplotlib figure on page 4, 6, 8 with optimal layout.
    """
    add_header(slide, f"【原圖精緻重繪】{fig_num_str}: {title_text}", category_text, sub_title)
    
    # Outer Card Container
    card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.75), Inches(11.733), Inches(5.2))
    card.fill.solid()
    card.fill.fore_color.rgb = BG_CARD
    card.line.color.rgb = BORDER_CARD
    card.line.width = Pt(1)
    
    if os.path.exists(fig_img_path):
        from PIL import Image
        img = Image.open(fig_img_path)
        w_px, h_px = img.size
        aspect = w_px / h_px
        
        if aspect > 1.85:
            # Figure 1 / Figure 2 Split Layout: Picture on Left, Architectural Commentary on Right!
            # Completely eliminates any vertical text overlap or boundary collision.
            pic_left = 1.05
            pic_top = 1.95
            pic_w = 6.80
            pic_h = min(4.80, pic_w / aspect)
            # Center the picture vertically in the 5.2" container
            pic_top_centered = 1.75 + (5.2 - pic_h) / 2
            slide.shapes.add_picture(fig_img_path, Inches(pic_left), Inches(pic_top_centered), width=Inches(pic_w), height=Inches(pic_h))
            
            # Commentary Card on Right
            card_right_x = 8.15
            card_right_w = 4.38
            tb = slide.shapes.add_textbox(Inches(card_right_x), Inches(1.85), Inches(card_right_w), Inches(5.0))
            tf = tb.text_frame
            tf.word_wrap = True
            
            p_cap = tf.paragraphs[0]
            r_c = p_cap.add_run()
            r_c.text = f"✦ 論文官方題註 (Caption)：\n{original_caption}\n"
            r_c.font.name = FONT_HEADING
            r_c.font.size = Pt(10)
            r_c.font.bold = True
            r_c.font.color.rgb = BRAND_TERRA
            
            p_head = tf.add_paragraph()
            p_head.space_before = Pt(6)
            r_h = p_head.add_run()
            r_h.text = "✦ 研析見解與核心意涵："
            r_h.font.name = FONT_HEADING
            r_h.font.size = Pt(11)
            r_h.font.bold = True
            r_h.font.color.rgb = BRAND_SAGE
            
            for ins in insights:
                p = tf.add_paragraph()
                p.space_before = Pt(5)
                r = p.add_run()
                r.text = f"• {ins}"
                r.font.name = FONT_BODY
                r.font.size = Pt(9.5)
                r.font.color.rgb = TEXT_BODY
        else:
            # Tall/Square diagram (e.g. Figure 6): Left picture, Right commentary
            img_left = 1.05
            img_top = 1.90
            img_h = 4.90
            img_w = min(6.8, img_h * aspect)
            slide.shapes.add_picture(fig_img_path, Inches(img_left), Inches(img_top), width=Inches(img_w), height=Inches(img_h))
            
            tb = slide.shapes.add_textbox(Inches(img_left + img_w + 0.35), Inches(1.90), Inches(11.733 - (img_w + 0.6)), Inches(4.90))
            tf = tb.text_frame
            tf.word_wrap = True
            
            p_cap = tf.paragraphs[0]
            r_c = p_cap.add_run()
            r_c.text = f"✦ 論文官方題註 (Caption)：\n{original_caption}\n"
            r_c.font.name = FONT_HEADING
            r_c.font.size = Pt(10.5)
            r_c.font.bold = True
            r_c.font.color.rgb = BRAND_TERRA
            
            p_head = tf.add_paragraph()
            p_head.space_before = Pt(8)
            r_h = p_head.add_run()
            r_h.text = "✦ 原圖拓撲與工程細節研析："
            r_h.font.name = FONT_HEADING
            r_h.font.size = Pt(11.5)
            r_h.font.bold = True
            r_h.font.color.rgb = BRAND_SAGE
            
            for ins in insights:
                p = tf.add_paragraph()
                p.space_before = Pt(6)
                r = p.add_run()
                r.text = f"• {ins}"
                r.font.name = FONT_BODY
                r.font.size = Pt(10.5)
                r.font.color.rgb = TEXT_BODY

def generate_entire_deck():
    prs = init_presentation()
    blank_layout = prs.slide_layouts[6]
    
    # -------------------------------------------------------------
    # SLIDE 1: 封面 (Title Slide)
    # -------------------------------------------------------------
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
    r_t.text = "✦  arXiv:2609.00006v1 學術全景重磅解析"
    r_t.font.name = FONT_HEADING
    r_t.font.size = Pt(11)
    r_t.font.bold = True
    r_t.font.color.rgb = BRAND_SAGE
    
    tb1 = s1.shapes.add_textbox(Inches(1.3), Inches(2.25), Inches(10.7), Inches(2.5))
    tf1 = tb1.text_frame
    tf1.word_wrap = True
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
    r_desc.text = "11 款生產級 Harness 原始碼解剖 · 13 項跨系統觀察 · 29 項設計模式 · 全套 18 表解析 · 18 條設計建議"
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
    p_m = tf_meta.paragraphs[0]
    r_m = p_m.add_run()
    r_m.text = "論文：arXiv:2609.00006v1（作者與機構請以 arXiv 摘要頁為準；版本釘選 2026 年 7 月）\n研究範疇：七大子系統 (D1-D7)、雙重缺席 (零 Agentic Framework / 零向量代碼 RAG)、平台化轉型論題 (Tool → Platform)"
    r_m.font.name = FONT_BODY
    r_m.font.size = Pt(10)
    r_m.font.color.rgb = TEXT_MUTED
    add_footer(s1, 1)

    # -------------------------------------------------------------
    # SLIDE 2: 核心命題與定義澄清 (Core Thesis & Definitions)
    # -------------------------------------------------------------
    s2 = prs.slides.add_slide(blank_layout)
    apply_warm_background(s2)
    add_header(s2, "核心命題與定義界定：Agent = Model + Harness", "理論基礎", "Harness 是模型以外的一切；釐清與 Scaffold、Framework、Eval Harness、Orchestrator 的四個邊界案例")
    add_enlarged_bullet_card(
        s2, left=0.8, top=1.75, width=5.7, height=4.1,
        title="1. 定義：Agent = Model + Harness (§2.1)",
        items=[
            "核心公式等式：Agent = Model + Harness，兩者缺一不可。",
            "模型提供智慧：Harness 是「模型以外的一切」，即把 LLM 接上世界的 Runtime。",
            "Harness 六大面向：迴圈、工具、上下文管理、安全控制、協調與擴展介面。",
            "複雜度不預測績效：約百行的 Mini-SWE-Agent 自報成績與大三個數量級的系統同級 (§2.4)。"
        ],
        tag="CORE THESIS",
        accent_color=BRAND_SAGE
    )
    add_enlarged_bullet_card(
        s2, left=6.833, top=1.75, width=5.7, height=4.1,
        title="2. 四大混淆術語邊界澄清 (Clarifying Terms)",
        items=[
            "Harness vs Scaffold：兩者近義；Scaffold 指結構程式碼（迴圈、註冊表），Harness 指出貨的完整 Runtime 產品。",
            "Harness vs Framework (LangChain 等)：Framework 是被 import 的函式庫；Harness 是開發者身處其中的 Runtime。",
            "Harness vs Eval Harness (SWE-bench)：評測 Harness 包裹 Agent 跑任務；Agent Harness 包裹模型使其行動，方向相反。",
            "Harness vs Orchestrator：Orchestrator / Meta-Harness 從上方協調多個 Harness，本身不實作編輯迴圈 (如 Omnigent)。"
        ],
        tag="TAXONOMY",
        accent_color=BRAND_TERRA
    )
    add_centered_quote_card(
        s2, left=0.8, top=6.0, width=11.733, height=0.95,
        en_quote="The model supplies the intelligence; the harness turns that intelligence into work.",
        highlight_word="turns that intelligence into work",
        zh_quote="模型提供智慧；Harness 透過迴圈、工具、上下文管理、安全控制、協調與擴展介面，把智慧轉化為工作。"
    )
    add_footer(s2, 2)

    # -------------------------------------------------------------
    # SLIDE 3: 【Table 2 全表深度解析】更廣闊的 Harness 生態版圖 (Side-by-Side)
    # -------------------------------------------------------------
    s3 = prs.slides.add_slide(blank_layout)
    apply_warm_background(s3)
    add_table_slide_adaptive(
        s3,
        tid="S3.T2",
        title="【Table 2 解析】2026 年中更廣闊的 Harness 市場全景版圖",
        category="學術表格解析",
        sub_title="Table 2: The Broader Coding-Agent Harness Landscape (Non-corpus Systems)",
        insights=[
            "原廠全面進場：2026/7 市場掃描發現逾兩打活躍 Harness；Google Antigravity CLI、GitHub Copilot CLI、xAI Grok Build、Amazon Kiro CLI 等皆已推出。",
            "開源重心：Cline (~64k)、Goose (捐贈 Linux Foundation)、Claw Code (~100k+) 與 Qwen Code / Kimi CLI / Trae Agent 等中國廠商 CLI。",
            "市場整併：SpaceX 併購 xAI 並宣布 600 億美元收購 Cursor；Gemini CLI 轉向閉源 Antigravity CLI（論文註：市場事件未經原始碼驗證）。"
        ],
        font_size=7.0,
        col_widths=[1.5, 1.2, 0.6, 0.8, 3.2],
        side_by_side=True
    )
    add_footer(s3, 3)

    # -------------------------------------------------------------
    # SLIDE 4: 【Table 3 全表深度解析】研究對象篩選準則與版本 (Side-by-Side)
    # -------------------------------------------------------------
    s4 = prs.slides.add_slide(blank_layout)
    apply_warm_background(s4)
    add_table_slide_adaptive(
        s4,
        tid="S4.T3",
        title="【Table 3 解析】11 款系統入選準則、Commit 版本與代表性",
        category="學術表格解析",
        sub_title="Table 3: System Selection Criteria and Repository Snapshots",
        insights=[
            "多樣性：涵蓋 TypeScript (Claude Code, Gemini CLI, OpenCode, Pi, OpenClaw)、Python (OpenHands, Aider, Vibe, Mini-SWE, Hermes) 與 Rust (Codex)。",
            "版本釘選：全部釘選於 2026 年 7 月 Release；原 8 個系統保留 4 月快照，構成跨一季（約 90 天）的縱向原始碼 diff 樣本。",
            "Omnigent (Databricks) 為對照點：自身無編輯迴圈，於統一 API 後協調 11 款廠商 Harness（含本研究 5 款），是首個 Meta-Harness。"
        ],
        font_size=8.0,
        col_widths=[1.4, 1.6, 0.8, 1.6, 1.9],
        side_by_side=True
    )
    add_footer(s4, 4)

    # -------------------------------------------------------------
    # SLIDE 5: 【重繪論文圖一】D1-D7 標準子系統架構圖 (Figure 1 Re-drawn)
    # -------------------------------------------------------------
    s5 = prs.slides.add_slide(blank_layout)
    apply_warm_background(s5)
    add_header(s5, "【重繪論文圖一】Harness 七大標準子系統架構全景", "論文圖一重繪", "Figure 1: The Canonical Anatomy and Architecture of Coding Agent Harnesses")
    harness_box = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.75), Inches(11.733), Inches(5.2))
    harness_box.fill.solid()
    harness_box.fill.fore_color.rgb = BG_CARD
    harness_box.line.color.rgb = BRAND_SAGE
    harness_box.line.width = Pt(1.5)
    
    h_label = s5.shapes.add_textbox(Inches(1.0), Inches(1.82), Inches(11.333), Inches(0.32))
    tf_hl = h_label.text_frame
    p_hl = tf_hl.paragraphs[0]
    r_hl = p_hl.add_run()
    r_hl.text = "THE HARNESS RUNTIME BOUNDARY (七大子系統 + 介面層 + Session Substrate)"
    r_hl.font.name = FONT_HEADING
    r_hl.font.size = Pt(10.5)
    r_hl.font.bold = True
    r_hl.font.color.rgb = BRAND_SAGE
    
    d1_card = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.1), Inches(2.20), Inches(11.133), Inches(0.85))
    d1_card.fill.solid()
    d1_card.fill.fore_color.rgb = RGBColor(0xEA, 0xF0, 0xEC)
    d1_card.line.color.rgb = BRAND_SAGE
    d1_card.line.width = Pt(1.2)
    tf_d1 = d1_card.text_frame
    p_d1 = tf_d1.paragraphs[0]
    p_d1.alignment = PP_ALIGN.CENTER
    r_d1 = p_d1.add_run()
    r_d1.text = "D1. Agent Loop (核心驅動引擎 / 狀態機迴圈)\n"
    r_d1.font.name = FONT_HEADING
    r_d1.font.size = Pt(11)
    r_d1.font.bold = True
    r_d1.font.color.rgb = BRAND_SLATE
    r_d1_sub = p_d1.add_run()
    r_d1_sub.text = "Iterative / Reflection / Coordinator-Worker · Stuck Detector · 回合與成本上限 · Middleware Pipeline"
    r_d1_sub.font.name = FONT_BODY
    r_d1_sub.font.size = Pt(9.5)
    r_d1_sub.font.color.rgb = TEXT_BODY
    
    mid_w = 3.55
    mid_gap = 0.24
    d2_card = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.1), Inches(3.20), Inches(mid_w), Inches(1.55))
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
    r_d2_t.font.size = Pt(10.5)
    r_d2_t.font.bold = True
    r_d2_t.font.color.rgb = BRAND_TERRA
    p_d2_b = tf_d2.add_paragraph()
    r_d2_b = p_d2_b.add_run()
    r_d2_b.text = "✦ 單原廠緊耦合 vs 多模型抽象\n✦ 靜態/動態 Prompt Cache 邊界\n✦ 反鍍金規則 (Anti-Gold-Plating)\n✦ Extended Thinking / Reasoning Effort"
    r_d2_b.font.name = FONT_BODY
    r_d2_b.font.size = Pt(9)
    r_d2_b.font.color.rgb = TEXT_BODY
    
    d4_card = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.1 + mid_w + mid_gap), Inches(3.20), Inches(mid_w), Inches(1.55))
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
    r_d4_t.font.size = Pt(10.5)
    r_d4_t.font.bold = True
    r_d4_t.font.color.rgb = BRAND_SAGE
    p_d4_b = tf_d4.add_paragraph()
    r_d4_b = p_d4_b.add_run()
    r_d4_b.text = "✦ 閾值壓縮 (7/11 系統採用)\n✦ 增量合併摘要 (Pi / OpenCode)\n✦ Gemini CLI：50% 觸發留最近 30%\n✦ 持久記憶寫入路徑 (新前沿)"
    r_d4_b.font.name = FONT_BODY
    r_d4_b.font.size = Pt(9)
    r_d4_b.font.color.rgb = TEXT_BODY
    
    d3_card = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.1 + (mid_w + mid_gap)*2), Inches(3.20), Inches(mid_w), Inches(1.55))
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
    r_d3_t.font.size = Pt(10.5)
    r_d3_t.font.bold = True
    r_d3_t.font.color.rgb = BRAND_OCHRE
    p_d3_b = tf_d3.add_paragraph()
    r_d3_b = p_d3_b.add_run()
    r_d3_b.text = "✦ 工具數光譜：1 個 bash 至 109+\n✦ 精確唯一子字串替換 (Frontier)\n✦ 模糊瀑布 (OpenCode Lev. 0.65)\n✦ 逾 ~15 個工具啟用遞延加載"
    r_d3_b.font.name = FONT_BODY
    r_d3_b.font.size = Pt(9)
    r_d3_b.font.color.rgb = TEXT_BODY
    
    d5_card = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.1), Inches(4.90), Inches(mid_w), Inches(1.55))
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
    r_d5_t.font.size = Pt(10.5)
    r_d5_t.font.bold = True
    r_d5_t.font.color.rgb = BRAND_TERRA
    p_d5_b = tf_d5.add_paragraph()
    r_d5_b = p_d5_b.add_run()
    r_d5_b.text = "✦ Starlark 策略與內嵌測試案例\n✦ Guardian LLM 審批 (Codex)\n✦ OS 級沙盒 (Bubblewrap/Seatbelt)\n✦ 互動式人工審批 (HITL)"
    r_d5_b.font.name = FONT_BODY
    r_d5_b.font.size = Pt(9)
    r_d5_b.font.color.rgb = TEXT_BODY
    
    d6_card = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.1 + mid_w + mid_gap), Inches(4.90), Inches(mid_w), Inches(1.55))
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
    r_d6_t.font.size = Pt(10.5)
    r_d6_t.font.bold = True
    r_d6_t.font.color.rgb = BRAND_SAGE
    p_d6_b = tf_d6.add_paragraph()
    r_d6_b = p_d6_b.add_run()
    r_d6_b.text = "✦ 六種模式 (9/11 支援多代理)\n✦ 遞迴組合 (Claude Code)\n✦ 線程樹 + CSV fan-out (Codex)\n✦ 子代理協同 8/9 維持行程內"
    r_d6_b.font.name = FONT_BODY
    r_d6_b.font.size = Pt(9)
    r_d6_b.font.color.rgb = TEXT_BODY
    
    d7_card = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.1 + (mid_w + mid_gap)*2), Inches(4.90), Inches(mid_w), Inches(1.55))
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
    r_d7_t.font.size = Pt(10.5)
    r_d7_t.font.bold = True
    r_d7_t.font.color.rgb = BRAND_SLATE
    p_d7_b = tf_d7.add_paragraph()
    r_d7_b = p_d7_b.add_run()
    r_d7_b.text = "✦ SKILL.md 技能標準 (9/11)\n✦ MCP 外部整合協議 (8/11)\n✦ 技能遞延載入 (9 家中 8 家)\n✦ Lifecycle Hooks (9/11)"
    r_d7_b.font.name = FONT_BODY
    r_d7_b.font.size = Pt(9)
    r_d7_b.font.color.rgb = TEXT_BODY
    add_footer(s5, 5)

    # -------------------------------------------------------------
    # SLIDE 6: 【原圖精緻重繪】圖一 (Figure 1 Matplotlib Redraw)
    # -------------------------------------------------------------
    s6 = prs.slides.add_slide(blank_layout)
    apply_warm_background(s6)
    add_matplotlib_figure_slide(
        s6,
        fig_img_path="fig1_matplotlib.png",
        fig_num_str="Figure 1",
        title_text="編程智慧體 Harness 標準解剖學架構全貌",
        category_text="論文圖形重繪",
        sub_title="Figure 1: The Canonical Anatomy of a Coding-Agent Harness (arXiv:2609.00006v1)",
        original_caption="The canonical anatomy of a coding-agent harness: seven subsystems around an agent loop, plus the interface layer and the session substrate.",
        insights=[
            "【圖中核心概念】Agent = Model + Harness：Harness 是模型以外的一切——迴圈、工具、上下文、安全、協調與擴展介面。論文主張七大子系統即此產物的標準解剖：最小實作顯示每項可縮到多小（協調可刻意缺席），最大實作顯示工程空間所在。",
            "向心解剖學架構：精準呈現以 Agent Loop (D1) 為心臟的向心閉環，向外輻射調度模型 (D2)、工具 (D3)、記憶 (D4)、安全 (D5)、多代理 (D6) 與擴展 (D7)。",
            "雙大貫穿基底：介面層 (TUI/IDE/SDK/Server) 與會話基底 (Session Substrate 軌跡持久化與分支樹) 橫切貫穿所有子系統。"
        ]
    )
    add_footer(s6, 6)

    # -------------------------------------------------------------
    # SLIDE 7: 【Table 1 全表深度解析】七大子系統極小與極大形式
    # -------------------------------------------------------------
    s7 = prs.slides.add_slide(blank_layout)
    apply_warm_background(s7)
    add_table_slide_adaptive(
        s7,
        tid="S2.T1",
        title="【Table 1 解析】七大子系統極小與極大實作光譜對照",
        category="學術表格解析",
        sub_title="Table 1: Component Map of a Coding-Agent Harness (Minimal vs. Maximal)",
        insights=[
            "光譜跨越 3 個數量級：Mini-SWE-Agent 約 100 行即實作全部七子系統；最大實作為百萬行級生產 CLI（Codex 約 1.1M 行 Rust）。",
            "可選擇性缺席：七子系統中僅協調 (D6) 可縮至刻意缺席（Mini-SWE-Agent、Aider、Pi 核心皆為單代理）。",
            "下限與生產系統的差距不在任務完成，而在安全、復原、成本管理、擴展性與平台介面 (§2.4)；可由 Minimal Form 起步逐步演進。"
        ],
        font_size=8.5,
        col_widths=[1.6, 3.8, 3.0, 3.8, 0.6],
        side_by_side=False
    )
    add_footer(s7, 7)

    # -------------------------------------------------------------
    # SLIDE 8: 【Table 4 全表深度解析】11 款系統高階特性與簽名能力 (Side-by-Side)
    # -------------------------------------------------------------
    s8 = prs.slides.add_slide(blank_layout)
    apply_warm_background(s8)
    add_table_slide_adaptive(
        s8,
        tid="S5.T4",
        title="【Table 4 解析】11 款系統高階架構特性與招牌特徵比較",
        category="學術表格解析",
        sub_title="Table 4: High-level Comparison and Signature Capabilities Across Corpus",
        insights=[
            "原廠招牌：Claude Code 為遞延工具載入與共享 prompt cache 的 fork；Codex 為代理維護的跨會話記憶與 V8 執行的工具呼叫。",
            "開源招牌：OpenHands 資源鎖並行工具、可託管競品 Harness；Aider 13 種多型編輯格式與唯一的排序式 repo map。",
            "極簡派：Mini-SWE-Agent 百行實作全部七子系統；Pi「一切皆擴展」核心與 session-tree 版本控制。"
        ],
        font_size=6.5,
        col_widths=[1.1, 0.7, 0.7, 0.8, 0.7, 0.7, 1.0, 0.8, 1.5],
        side_by_side=True
    )
    add_footer(s8, 8)

    # -------------------------------------------------------------
    # SLIDE 9: 【重繪論文圖二】三種驅動迴圈範式對比 (Figure 2 Re-drawn)
    # -------------------------------------------------------------
    s9 = prs.slides.add_slide(blank_layout)
    apply_warm_background(s9)
    add_header(s9, "【重繪論文圖二】三種驅動迴圈範式對比 (Figure 2)", "迴圈架構", "Figure 2: Contrasting Iterative ReAct, Reflection-Augmented, and Coordinator-Worker Loops")
    col3_w = 3.75
    col3_gap = 0.24
    
    p1 = s9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.75), Inches(col3_w), Inches(5.2))
    p1.fill.solid()
    p1.fill.fore_color.rgb = BG_CARD
    p1.line.color.rgb = BORDER_CARD
    p1.line.width = Pt(1)
    tb_p1 = s9.shapes.add_textbox(Inches(1.0), Inches(1.9), Inches(col3_w - 0.4), Inches(4.9))
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
    r_p1_sub.text = "代表：Mini-SWE-Agent, OpenHands, OpenCode\n"
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
    
    p2 = s9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8 + col3_w + col3_gap), Inches(1.75), Inches(col3_w), Inches(5.2))
    p2.fill.solid()
    p2.fill.fore_color.rgb = BG_CARD
    p2.line.color.rgb = BORDER_CARD
    p2.line.width = Pt(1)
    tb_p2 = s9.shapes.add_textbox(Inches(1.0 + col3_w + col3_gap), Inches(1.9), Inches(col3_w - 0.4), Inches(4.9))
    tf_p2 = tb_p2.text_frame
    tf_p2.word_wrap = True
    p2_0 = tf_p2.paragraphs[0]
    r_p2_0 = p2_0.add_run()
    r_p2_0.text = "範式 2: 反思增強迴圈\n(Reflection-Augmented)\n"
    r_p2_0.font.name = FONT_HEADING
    r_p2_0.font.size = Pt(12)
    r_p2_0.font.bold = True
    r_p2_0.font.color.rgb = BRAND_TERRA
    p2_sub = tf_p2.add_paragraph()
    r_p2_sub = p2_sub.add_run()
    r_p2_sub.text = "代表：Aider (run_one 核心), Hermes Verify\n"
    r_p2_sub.font.name = FONT_BODY
    r_p2_sub.font.size = Pt(9.5)
    r_p2_sub.font.color.rgb = BRAND_SAGE
    p2_flow = tf_p2.add_paragraph()
    p2_flow.space_before = Pt(8)
    r_flow2 = p2_flow.add_run()
    r_flow2.text = "【控制流程圖解】\n[LLM Edit Response]\n       ▼\n[Apply Diff Patch]\n       ▼\n[Run Linter & AST Syntax]\n       ▼\n[Run Test Suite (測試集)]\n       ▼ 失敗？\n[Reflected Feedback] 注入錯誤訊號\n       ▼ 重新請求 LLM (最多 3 次)\n\n✦ 優點：lint/測試訊號回饋自我修正\n✦ 缺點：耗費額外 Token 與執行時間"
    r_flow2.font.name = FONT_BODY
    r_flow2.font.size = Pt(10)
    r_flow2.font.color.rgb = TEXT_BODY
    
    p3 = s9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8 + (col3_w + col3_gap)*2), Inches(1.75), Inches(col3_w), Inches(5.2))
    p3.fill.solid()
    p3.fill.fore_color.rgb = BG_CARD
    p3.line.color.rgb = BORDER_CARD
    p3.line.width = Pt(1)
    tb_p3 = s9.shapes.add_textbox(Inches(1.0 + (col3_w + col3_gap)*2), Inches(1.9), Inches(col3_w - 0.4), Inches(4.9))
    tf_p3 = tb_p3.text_frame
    tf_p3.word_wrap = True
    p3_0 = tf_p3.paragraphs[0]
    r_p3_0 = p3_0.add_run()
    r_p3_0.text = "範式 3: 協調工兵派工\n(Coordinator-Worker)\n"
    r_p3_0.font.name = FONT_HEADING
    r_p3_0.font.size = Pt(12)
    r_p3_0.font.bold = True
    r_p3_0.font.color.rgb = BRAND_OCHRE
    p3_sub = tf_p3.add_paragraph()
    r_p3_sub = p3_sub.add_run()
    r_p3_sub.text = "代表：Claude Code, Codex, Hermes (設定啟用)\n"
    r_p3_sub.font.name = FONT_BODY
    r_p3_sub.font.size = Pt(9.5)
    r_p3_sub.font.color.rgb = BRAND_SLATE
    p3_flow = tf_p3.add_paragraph()
    p3_flow.space_before = Pt(8)
    r_flow3 = p3_flow.add_run()
    r_flow3.text = "【控制流程圖解】\n[Lead Coordinator] 接收總目標\n       ▼ 拆解為獨立子任務\n[Fork Sub-Agent Context]\n       ▼\n[Worker 1]    [Worker 2]    [Worker 3]\n(專門檢索)    (執行編譯)    (審核修改)\n       ▼             ▼             ▼\n[Task-Notification XML 摘要回傳]\n       ▼\n[Lead 合成結果並推進下一階段]\n\n✦ 優點：保護主 Context、並行探索\n✦ 缺點：協調複雜度高、Token 開銷大"
    r_flow3.font.name = FONT_BODY
    r_flow3.font.size = Pt(10)
    r_flow3.font.color.rgb = TEXT_BODY
    add_footer(s9, 9)

    # -------------------------------------------------------------
    # SLIDE 10: 【原圖精緻重繪】圖二 (Figure 2 Matplotlib Redraw)
    # -------------------------------------------------------------
    s10 = prs.slides.add_slide(blank_layout)
    apply_warm_background(s10)
    add_matplotlib_figure_slide(
        s10,
        fig_img_path="fig2_matplotlib.png",
        fig_num_str="Figure 2",
        title_text="三大智慧體迴圈範式對比圖",
        category_text="論文圖形重繪",
        sub_title="Figure 2: Three Agent Loop Paradigms (arXiv:2609.00006v1)",
        original_caption="Three agent loop paradigms: (a) iterative action-observation, (b) reflection-augmented with external linter feedback, and (c) coordinator-worker with sub-agent dispatch.",
        insights=[
            "子圖 (a) 迭代迴圈：最經典的 Action-Observation 閉環，Stop 條件取決於 LLM 返回內容或預算計數器。",
            "子圖 (b) 反思迴圈：Aider 的核心貢獻在於將 Linter/測試錯誤反饋 (TreeContext) 作為下一次 Prompt 的第一公民，實現自我修復。",
            "子圖 (c) 協調者模式：Coordinator 派生 Worker 節點，非同步並行執行並透過 XML 摘要區塊回傳結果，保護主 Context 不被污染。"
        ]
    )
    add_footer(s10, 10)

    # -------------------------------------------------------------
    # SLIDE 11: 【Table 5 全表深度解析】驅動迴圈特徵詳細比較 (Side-by-Side)
    # -------------------------------------------------------------
    s11 = prs.slides.add_slide(blank_layout)
    apply_warm_background(s11)
    add_table_slide_adaptive(
        s11,
        tid="S6.T5",
        title="【Table 5 解析】各系統驅動迴圈型態、並行度與卡死偵測機制",
        category="學術表格解析",
        sub_title="Table 5: Detailed Agent Loop Characteristics Across Eleven Systems",
        insights=[
            "控制流分化：從簡單的 Async While-Loop 走向中間件管線 (Mistral Vibe) 與日誌即佇列 (OpenCode Log-as-Queue)。",
            "卡死偵測光譜：Claude Code 與 Codex 仍無自動卡死偵測；OpenHands 五情境 StuckDetector、Gemini CLI hash+LLM 混合偵測屬平台級投資。",
            "工具並行：Claude Code 以 isConcurrencySafe 分批（唯讀並行、寫入序列）；OpenHands 依資源加鎖；Pi 以 per-file 佇列序列化編輯。"
        ],
        font_size=7.0,
        col_widths=[1.3, 2.0, 1.6, 1.3, 1.1],
        side_by_side=True
    )
    add_footer(s11, 11)

    # -------------------------------------------------------------
    # SLIDE 12: 【Table 6 全表深度解析】提示詞組裝與工程架構 (Side-by-Side)
    # -------------------------------------------------------------
    s12 = prs.slides.add_slide(blank_layout)
    apply_warm_background(s12)
    add_table_slide_adaptive(
        s12,
        tid="S7.T6",
        title="【Table 6 解析】提示詞工程架構：分段、快取對齊與動態組裝",
        category="學術表格解析",
        sub_title="Table 6: Prompt Engineering Architectures Across Eleven Systems",
        insights=[
            "快取邊界：Claude Code 與 OpenHands 劃分「靜態前綴」與「動態後綴」以利快取命中；Hermes 以 bit-perfect 前綴正規化連本地 KV 快取都命中。",
            "Markdown 情境檔自動發現：管理 repo 情境的系統全數收斂於階層式 AGENTS.md / CLAUDE.md / GEMINI.md，且會讀取鄰居檔名。",
            "模板技術：仍以純 Markdown、Jinja2 或字串拼接為主；OpenHands 改用 PromptRegistry，Codex 提示詞改由伺服器模型目錄下發。"
        ],
        font_size=6.4,
        col_widths=[1.2, 2.0, 1.9, 1.3, 0.9],
        side_by_side=True
    )
    add_footer(s12, 12)

    # -------------------------------------------------------------
    # SLIDE 13: 【Table 16 全表深度解析】系統提示詞修辭規範與反鍍金
    # -------------------------------------------------------------
    s13 = prs.slides.add_slide(blank_layout)
    apply_warm_background(s13)
    add_table_slide_adaptive(
        s13,
        tid="A1.T16",
        title="【Table 16 解析】11 款系統提示詞修辭內容：反鍍金、精簡度與承諾策略",
        category="學術表格解析",
        sub_title="Table 16: Rhetorical Content of Eleven System Prompts (July 2026)",
        insights=[
            "精簡度：11 份中 9 份含字數指示；Claude Code ≤25/≤100 字規則僅限內部 A/B 版本；OpenCode「少於 4 行」最激進。",
            "Git Commit 共識瓦解：4 月提及 git 者皆禁自主 commit；7 月 Mistral Vibe 反轉、Codex 新版移除，但仍無系統允許自主 push。",
            "強調三流派：大寫標籤 (IMPORTANT:/NEVER；Claude Code、Codex、OpenHands、OpenCode)、結構化規則區塊、範例驅動。"
        ],
        font_size=7.2,
        col_widths=[1.8, 2.8, 2.0, 2.3, 1.3, 1.533],
        side_by_side=False
    )
    add_footer(s13, 13)

    # -------------------------------------------------------------
    # SLIDE 14: 【Table 17 全表深度解析】高級 API 原生特性的深度調用
    # -------------------------------------------------------------
    s14 = prs.slides.add_slide(blank_layout)
    apply_warm_background(s14)
    add_table_slide_adaptive(
        s14,
        tid="A1.T17",
        title="【Table 17 解析】各系統對底層 LLM 進階 API 物理特性的調用光譜",
        category="學術表格解析",
        sub_title="Table 17: Advanced API Features Used by Each System (July 2026)",
        insights=[
            "快取路線分歧：Claude Code 用 Blake2b 靜態/動態邊界；Codex 用 ThreadId 衍生 prompt_cache_key；OpenCode 同時輸出六種快取方言。",
            "推理強度：Claude Code 暴露 budget_tokens；Codex 推理等級延伸至 max / ultra（ultra 會自動委派子代理）；Pi 統一為七級刻度。",
            "視覺：Mistral Vibe 新增剪貼簿貼圖與 ACP 內嵌影像；Aider 依模型啟用、Mini-SWE 為預設關閉選項，已無系統純文字限定。"
        ],
        font_size=7.4,
        col_widths=[1.5, 1.8, 1.2, 1.3, 1.4, 1.1, 1.0, 1.433],
        side_by_side=False
    )
    add_footer(s14, 14)

    # -------------------------------------------------------------
    # SLIDE 15: 【Table 7 全表深度解析】檔案編輯策略與補丁演進 (Side-by-Side)
    # -------------------------------------------------------------
    s15 = prs.slides.add_slide(blank_layout)
    apply_warm_background(s15)
    add_table_slide_adaptive(
        s15,
        tid="S8.T7",
        title="【Table 7 解析】檔案編輯策略演化：精確比對、Diff 與模糊寬容",
        category="學術表格解析",
        sub_title="Table 7: File Editing Strategies Across the Eleven Systems (July 2026)",
        insights=[
            "編輯版圖重組：11 系統共八種策略；Mistral Vibe 一季內刪除 SEARCH/REPLACE 工具，改採 Claude Code 式精確匹配。",
            "模糊瀑布家族：OpenCode 九階 cascade (Levenshtein 0.65)、Hermes 九策略鏈「inspired by OpenCode」；Aider RelativeIndenter + diff_match_patch (0.95)。",
            "Frontier 精確匹配：Claude Code、Mistral Vibe 採唯一子字串替換；Gemini CLI 以 LLM edit-fixer 修復失敗匹配，為第三條路線。"
        ],
        font_size=6.4,
        col_widths=[1.15, 1.6, 1.75, 1.35, 1.45],
        side_by_side=True
    )
    add_footer(s15, 15)

    # -------------------------------------------------------------
    # SLIDE 16: 【Table 8 全表深度解析】執行沙盒與微隔離機制 (Side-by-Side)
    # -------------------------------------------------------------
    s16 = prs.slides.add_slide(blank_layout)
    apply_warm_background(s16)
    add_table_slide_adaptive(
        s16,
        tid="S8.T8",
        title="【Table 8 解析】執行沙盒與隔離機制：Docker、Bubblewrap 與 Seatbelt",
        category="學術表格解析",
        sub_title="Table 8: Execution Sandboxing Mechanisms (July 2026)",
        insights=[
            "OS 沙盒免容器開銷：Codex（vendored Bubblewrap / Seatbelt / Windows restricted token）與 Gemini CLI 是僅有的兩家原生跨平台沙盒。",
            "網路與憑證：Codex 以 --unshare-net 與 network_rule 管控網路；Gemini CLI 執行前清除 TOKEN/SECRET/KEY 類環境變數。",
            "規模不等於沙盒：Hermes (~642K 行) 零 OS 隔離、OpenCode 僅有策略層；沙盒是選擇而非規模的必然 (Obs.6)。"
        ],
        font_size=6.8,
        col_widths=[1.05, 3.15, 1.9, 1.2],
        side_by_side=True
    )
    add_footer(s16, 16)

    # -------------------------------------------------------------
    # SLIDE 17: 【Table 13 全表深度解析】代碼檢索機制（告別向量 RAG）(Side-by-Side)
    # -------------------------------------------------------------
    s17 = prs.slides.add_slide(blank_layout)
    apply_warm_background(s17)
    add_table_slide_adaptive(
        s17,
        tid="S13.T13",
        title="【Table 13 解析】代碼檢索機制全景：確定性工具對向量 RAG 的全面替代",
        category="學術表格解析",
        sub_title="Table 13: Code-Retrieval Mechanisms in Lieu of Vector-based RAG",
        insights=[
            "向量檢索代碼 0/11：embeddings 僅見於對話記憶（OpenClaw 預設混合檢索、Hermes 選配插件），從不用於讀取原始碼。",
            "確定性檢索：全部依賴 ripgrep、tree-sitter、glob 與自動發現的 Markdown 情境檔；Aider RepoMap 為唯一排序式 repo map。",
            "原因：程式碼具確定性結構（路徑、LSP、tree-sitter）且分鐘級變動，預建 embeddings 幾乎必然過時 (§13.2)。"
        ],
        font_size=6.4,
        col_widths=[1.0, 2.3, 4.0],
        side_by_side=True
    )
    add_footer(s17, 17)

    # -------------------------------------------------------------
    # SLIDE 18: 缺席二：全面拋棄向量代碼檢索 (Observation 13.2)
    # -------------------------------------------------------------
    s18 = prs.slides.add_slide(blank_layout)
    apply_warm_background(s18)
    add_header(s18, "缺席之二：全面拋棄向量代碼檢索 (No Vector Code RAG)", "核心實證震撼", "ripgrep、tree-sitter、glob 與 Markdown 情境檔取代向量檢索 (Observation 9)")
    add_enlarged_bullet_card(
        s18, left=0.8, top=1.75, width=5.7, height=5.2,
        title="1. 向量代碼檢索 (Code RAG) 的失效本質",
        items=[
            "語法確定性：程式碼帶有路徑、LSP、tree-sitter 解析與型別等確定性結構，語意相似度無法複製。",
            "索引必然過時：程式碼分鐘級變動，預建 embeddings 幾乎「生來即過時」。",
            "收益不穩定：CodeRAG-Bench 顯示增益隨任務差異大，文件查詢有效，其餘邊際或無。",
            "營運成本：embedding 計算、向量庫維護與漂移管理，卻無邊際價值 (§13.2)。"
        ],
        tag="WHY VECTOR FAILS",
        accent_color=BRAND_TERRA
    )
    add_enlarged_bullet_card(
        s18, left=6.833, top=1.75, width=5.7, height=5.2,
        title="2. 一線 Harness 的確定性檢索武器庫",
        items=[
            "ripgrep / find / glob：每個開發環境已內建近乎最佳的檢索系統。",
            "tree-sitter 符號擷取：Aider RepoMap 以此建立依對話相關度排序的符號地圖。",
            "JIT 檢索：呼應 Anthropic 情境工程指引，按需以 grep / 檔案系統取得資訊。",
            "Markdown 情境檔：自動發現 AGENTS.md / CLAUDE.md 等階層檔並按需注入。"
        ],
        tag="DETERMINISTIC SUITE",
        accent_color=BRAND_SAGE
    )
    add_footer(s18, 18)

    # -------------------------------------------------------------
    # SLIDE 19: 【重繪圖四】四種記憶與上下文管理策略 (Figure 4)
    # -------------------------------------------------------------
    s19 = prs.slides.add_slide(blank_layout)
    apply_warm_background(s19)
    add_header(s19, "【重繪論文圖四】四種記憶與上下文管理策略 (Figure 4)", "記憶架構", "Figure 4: Four Practical Context Management Strategies in Increasing Sophistication")
    col4_w = 2.75
    col4_gap = 0.24
    strategies = [
        ("策略 1: 線性歷史\n(Linear History)", "Mini-SWE-Agent", "無限制線性增長，完全仰賴現代超長 Context (1M)。適合短期評測，長程必衰退。"),
        ("策略 2: 遞迴二分摘要\n(Recursive Halving)", "Aider (ChatSummary)", "超過上限（預設 1024）時依 token 對半切：保留最近 50%，前半以（可選弱模型）摘要，最多遞迴 3 層。"),
        ("策略 3: 可插拔壓縮器\n(Pluggable Condenser)", "OpenHands SDK", "抽象 Condenser 基類（V1 收斂為 3 種）；壓縮本身為可重放事件，並兼作溢位錯誤復原。"),
        ("策略 4: 閾值邊界壓縮\n(Threshold Compaction)", "Claude Code, Codex, Gemini", "Claude Code 於 13K tokens 緩衝內觸發：剝除圖片、LLM 摘要、插入邊界訊息，壓縮後還原最多 5 個檔案。")
    ]
    for idx, (st_t, st_rep, st_desc) in enumerate(strategies):
        x = 0.8 + idx * (col4_w + col4_gap)
        c = s19.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(x), Inches(1.75), Inches(col4_w), Inches(5.2))
        c.fill.solid()
        c.fill.fore_color.rgb = BG_CARD
        c.line.color.rgb = BORDER_CARD
        c.line.width = Pt(1)
        tb_c = s19.shapes.add_textbox(Inches(x + 0.15), Inches(1.9), Inches(col4_w - 0.3), Inches(4.9))
        tf_c = tb_c.text_frame
        tf_c.word_wrap = True
        p = tf_c.paragraphs[0]
        r = p.add_run()
        r.text = st_t + "\n"
        r.font.name = FONT_HEADING
        r.font.size = Pt(11.5)
        r.font.bold = True
        r.font.color.rgb = BRAND_SAGE if idx % 2 == 0 else BRAND_TERRA
        p_sub = tf_c.add_paragraph()
        r_sub = p_sub.add_run()
        r_sub.text = f"代表：{st_rep}\n"
        r_sub.font.name = FONT_BODY
        r_sub.font.size = Pt(9.5)
        r_sub.font.bold = True
        r_sub.font.color.rgb = TEXT_HEADLINE
        p_b = tf_c.add_paragraph()
        p_b.space_before = Pt(6)
        r_b = p_b.add_run()
        r_b.text = f"【架構原理】\n{st_desc}"
        r_b.font.name = FONT_BODY
        r_b.font.size = Pt(9.5)
        r_b.font.color.rgb = TEXT_BODY
    add_footer(s19, 19)

    # -------------------------------------------------------------
    # SLIDE 20: 【重繪圖五】Claude Code 與 Codex 安全防禦架構 (Figure 5)
    # -------------------------------------------------------------
    s20 = prs.slides.add_slide(blank_layout)
    apply_warm_background(s20)
    add_header(s20, "【重繪論文圖五】Claude Code 與 Codex 安全防禦棧 (Figure 5)", "安全架構", "Figure 5: Multi-Layered Permission Stacks and Sandboxing in Tier-1 Harnesses")
    box_cl = s20.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.75), Inches(5.7), Inches(5.2))
    box_cl.fill.solid()
    box_cl.fill.fore_color.rgb = BG_CARD
    box_cl.line.color.rgb = BORDER_CARD
    box_cl.line.width = Pt(1)
    tb_cl = s20.shapes.add_textbox(Inches(1.0), Inches(1.9), Inches(5.3), Inches(4.9))
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
    r_b.text = "✦ Layer 1: 宣告式權限比對 (Declarative Matching)\n   靜態 Glob 與前綴比對規則（如唯讀目錄、允許讀取白名單），未達模型即秒級放行或阻擋。\n\n✦ Layer 2: LLM 分類器 (論文 §10.2：Codex Guardian 對應此中層)\n   背景/fork 子代理僅開放 Layer 1~2（提示改判拒絕）；另有 Denial Tracking 累計拒絕後回退為提示。\n\n✦ Layer 3: 互動式人機提示 (Interactive Prompting)\n   高危動作（修改檔案、發送網路請求）向前台使用者彈出審查對話框；子代理遇阻則升級至父級協調器處理。\n\n★ 核心設計：權限狀態每代理隔離，杜絕非同步並行時的跨代理權限污染。"
    r_b.font.name = FONT_BODY
    r_b.font.size = Pt(10)
    r_b.font.color.rgb = TEXT_BODY
    
    box_cx = s20.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.833), Inches(1.75), Inches(5.7), Inches(5.2))
    box_cx.fill.solid()
    box_cx.fill.fore_color.rgb = BG_CARD
    box_cx.line.color.rgb = BORDER_CARD
    box_cx.line.width = Pt(1)
    tb_cx = s20.shapes.add_textbox(Inches(7.033), Inches(1.9), Inches(5.3), Inches(4.9))
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
    add_footer(s20, 20)

    # -------------------------------------------------------------
    # SLIDE 21: 【重繪論文圖六】六大多代理協同拓撲 (Figure 6 Re-drawn)
    # -------------------------------------------------------------
    s21 = prs.slides.add_slide(blank_layout)
    apply_warm_background(s21)
    add_header(s21, "【重繪論文圖六】六大多智慧體協同拓撲全景 (Figure 6)", "拓撲架構", "Figure 6: Multi-Agent Topology Archetypes Across Eleven Production Systems")
    topo_w = 3.75
    topo_h = 2.45
    topo_gap_x = 0.24
    topo_gap_y = 0.20
    topos = [
        ("1. 單代理獨立迴圈 (Single-agent)", "Mini-SWE-Agent, Aider, Pi", "無派工工具 (No Spawn Tool)，專注單一 Context 反覆迭代，排除多代理複雜性。", BRAND_SAGE),
        ("2. 循序委託 (Sequential)", "Mistral Vibe (task tool)", "父代理啟動單一子代理，父級阻塞等待；子代理回傳摘要後銷毀，單次僅一個活躍。", BRAND_TERRA),
        ("3. 並行子會話 (Parallel Sessions)", "OpenHands, OpenCode", "父代理並行發起多個工作 Session，各自維護獨立歷史記錄，並行執行加速探索。", BRAND_OCHRE),
        ("4. 階層式線程樹 (Thread Tree)", "Codex CLI", "專屬執行緒，深度追蹤、fork mode 控制繼承、CSV map-reduce fan-out 並持久化父子拓撲。", BRAND_SLATE),
        ("5. 遞迴組合 (Recursive)", "Claude Code", "任何 Agent 皆可再遞迴生成子 Agent；跨 Fork 共享 System Prompt 快取，XML 摘要回傳。", BRAND_SAGE),
        ("6. 註冊表與跨行程協議", "Gemini CLI, OpenClaw, Hermes", "透過 Agent 註冊表依名稱調度，跨行程邊界透過 ACP / A2A / SQLite 協同通訊。", BRAND_TERRA)
    ]
    for idx, (t_title, t_rep, t_desc, t_color) in enumerate(topos):
        row = idx // 3
        col = idx % 3
        x = 0.8 + col * (topo_w + topo_gap_x)
        y = 1.75 + row * (topo_h + topo_gap_y)
        card = s21.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(x), Inches(y), Inches(topo_w), Inches(topo_h))
        card.fill.solid()
        card.fill.fore_color.rgb = BG_CARD
        card.line.color.rgb = BORDER_CARD
        card.line.width = Pt(1)
        tb = s21.shapes.add_textbox(Inches(x + 0.15), Inches(y + 0.12), Inches(topo_w - 0.3), Inches(topo_h - 0.24))
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
    add_footer(s21, 21)

    # -------------------------------------------------------------
    # SLIDE 22: 【原圖精緻重繪】圖六 (Figure 6 Matplotlib Redraw)
    # -------------------------------------------------------------
    s22 = prs.slides.add_slide(blank_layout)
    apply_warm_background(s22)
    add_matplotlib_figure_slide(
        s22,
        fig_img_path="fig6_matplotlib.png",
        fig_num_str="Figure 6",
        title_text="六大多智慧體協同拓撲架構圖論",
        category_text="論文圖形重繪",
        sub_title="Figure 6: The Six Multi-Agent Orchestration Patterns (arXiv:2609.00006v1)",
        original_caption="The six multi-agent orchestration patterns: red nodes spawn, blue nodes execute actions, dashed boxes represent process or session boundaries.",
        insights=[
            "拓撲節點定義：紅色為派工節點 (Spawn)，藍色為執行動作 (Action)，虛線框代表進程或會話邊界。",
            "極簡陣營的自律：單代理與循序委託徹底避免非同步分支導致的狀態競爭與 Context 膨脹。",
            "優化取向不同：Claude Code fork 共享 prompt cache（成本）；Codex 以 SpawnAgentForkMode (FullHistory / LastNTurns) 控制繼承。"
        ]
    )
    add_footer(s22, 22)

    # -------------------------------------------------------------
    # SLIDE 23: 【重繪圖七】協調者與工兵派工流 (Figure 7)
    # -------------------------------------------------------------
    s23 = prs.slides.add_slide(blank_layout)
    apply_warm_background(s23)
    add_header(s23, "【重繪論文圖七】協調者與工兵四階段派工流 (Figure 7)", "派工流模型", "Figure 7: Lead Agent Orchestrating Whitelisted Workers through Structured Phases")
    lead_box = s23.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.75), Inches(11.733), Inches(1.3))
    lead_box.fill.solid()
    lead_box.fill.fore_color.rgb = RGBColor(0xEA, 0xF0, 0xEC)
    lead_box.line.color.rgb = BRAND_SAGE
    lead_box.line.width = Pt(1.5)
    tb_lead = s23.shapes.add_textbox(Inches(1.0), Inches(1.85), Inches(11.333), Inches(1.1))
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
    r_l_desc.text = "Coordinator Mode 啟用後，Lead 依 Research → Synthesis → Implementation → Verification 推進；Worker 限 16 工具白名單，以 <task-notification> XML 回報。"
    r_l_desc.font.name = FONT_BODY
    r_l_desc.font.size = Pt(10)
    r_l_desc.font.color.rgb = TEXT_BODY
    
    stage_w = 2.75
    stage_gap = 0.24
    stages = [
        ("階段 1: Research (調研)", "調研 Worker", ["FileRead, Grep, Glob", "WebSearch, WebFetch", "平行探索程式碼庫", "以 XML 通知回報發現"], BRAND_SAGE),
        ("階段 2: Synthesis (合成)", "主協調者決策", ["Lead 彙整 Worker 發現", "合成後才委派下一階段", "確定方案與修改範圍", "保護主 Context 精簡"], BRAND_TERRA),
        ("階段 3: Implement (實作)", "受限寫入工兵", ["FileEdit, FileWrite", "Bash, PowerShell", "Enter/ExitWorktree", "限 16 工具白名單"], BRAND_OCHRE),
        ("階段 4: Verification (校驗)", "測試與審查工兵", ["執行測試驗證結果", "內建 VerificationAgent", "Lead 判定是否完成", "完成交付閉環"], BRAND_SLATE)
    ]
    for idx, (s_title, s_sub, s_items, s_color) in enumerate(stages):
        sx = 0.8 + idx * (stage_w + stage_gap)
        scard = s23.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(sx), Inches(3.25), Inches(stage_w), Inches(3.7))
        scard.fill.solid()
        scard.fill.fore_color.rgb = BG_CARD
        scard.line.color.rgb = BORDER_CARD
        scard.line.width = Pt(1)
        tb_s = s23.shapes.add_textbox(Inches(sx + 0.15), Inches(3.4), Inches(stage_w - 0.3), Inches(3.4))
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
    add_footer(s23, 23)

    # -------------------------------------------------------------
    # SLIDE 24: 【Table 9 全表深度解析】多代理協同架構詳細對比 (Side-by-Side)
    # -------------------------------------------------------------
    s24 = prs.slides.add_slide(blank_layout)
    apply_warm_background(s24)
    add_table_slide_adaptive(
        s24,
        tid="S11.T9",
        title="【Table 9 解析】九大多智慧體系統協同機制、通訊與工具過濾 (1/2)",
        category="學術表格解析",
        sub_title="Table 9: Multi-Agent Orchestration Across Nine Multi-Agent Systems",
        insights=[
            "行程內協同為主流：9 個多代理系統中 8 個以行程內原語或非標準協定（Pi JSONL、Hermes SQLite）協調子代理。",
            "工具約束：Claude Code Worker 限 16 工具白名單；Hermes 子代理工具取父級交集並封鎖 6 項工具（禁遞迴、禁寫記憶）。",
            "快取無縫繼承：父代理在 Fork 子代理時，原樣凍結父級已編譯的 System Prompt，確保子代理首輪命中快取。"
        ],
        font_size=7.5,
        col_widths=[0.95, 1.5, 1.5, 1.45, 1.05, 1.0],
        side_by_side=True,
        row_range=(0, 5)
    )
    add_footer(s24, 24)

    s24b = prs.slides.add_slide(blank_layout)
    apply_warm_background(s24b)
    add_table_slide_adaptive(
        s24b,
        tid="S11.T9",
        title="【Table 9 解析】九大多智慧體系統協同機制、通訊與工具過濾 (2/2)",
        category="學術表格解析",
        sub_title="Table 9: Multi-Agent Orchestration Across Nine Multi-Agent Systems",
        insights=[
            "行程內協同為主流：9 個多代理系統中 8 個以行程內原語或非標準協定（Pi JSONL、Hermes SQLite）協調子代理。",
            "工具約束：Claude Code Worker 限 16 工具白名單；Hermes 子代理工具取父級交集並封鎖 6 項工具（禁遞迴、禁寫記憶）。",
            "快取無縫繼承：父代理在 Fork 子代理時，原樣凍結父級已編譯的 System Prompt，確保子代理首輪命中快取。"
        ],
        font_size=7.5,
        col_widths=[0.95, 1.5, 1.5, 1.45, 1.05, 1.0],
        side_by_side=True,
        row_range=(5, None)
    )
    add_footer(s24b, 24)

    # -------------------------------------------------------------
    # SLIDE 25: 【Table 14 全表深度解析】主從代理通訊與協議定位
    # -------------------------------------------------------------
    s25 = prs.slides.add_slide(blank_layout)
    apply_warm_background(s25)
    add_table_slide_adaptive(
        s25,
        tid="S13.T14",
        title="【Table 14 解析】主從代理通訊機制與協議部署定位",
        category="學術表格解析",
        sub_title="Table 14: Main-Agent to Sub-Agent Communication and Protocol Placement",
        insights=[
            "內部通訊維持行程內：8/9 的多代理系統內部協同堅持使用 In-process Primitives，避免跨行程 RPC 開銷。",
            "ACP 已在 6/11 系統出貨並承擔三角色：編輯器↔Agent、Harness 託管（OpenHands 託管 Claude Code/Codex/Gemini）、A2A 跨廠網格（僅 Gemini）。",
            "實務建議 (Rec 13)：建 ACP Server 一次取得 IDE、宿主與 Meta-Harness 三類受眾；子代理維持行程內。"
        ],
        font_size=8.2,
        col_widths=[1.8, 4.5, 3.8, 1.633],
        side_by_side=False
    )
    add_footer(s25, 25)

    # -------------------------------------------------------------
    # SLIDE 26: 【Table 10 全表深度解析】技能 (Skills) 支援與規格遵循 (Side-by-Side)
    # -------------------------------------------------------------
    s26 = prs.slides.add_slide(blank_layout)
    apply_warm_background(s26)
    add_table_slide_adaptive(
        s26,
        tid="S12.T10",
        title="【Table 10 解析】技能體系 (Skills) 支援、發現路徑與加載規範 (1/2)",
        category="學術表格解析",
        sub_title="Table 10: Skills Support Across Eleven Systems (Spec Conformance)",
        insights=[
            "SKILL.md 成事實標準：9/11 支援（僅 Aider、Mini-SWE 缺席）；6 家接受 `.agents/skills/`，OpenCode 還讀取 `~/.claude/skills`。",
            "YAML Frontmatter 元資料治理：透過 name、description、paths 與 requires 定義前置觸發條件。",
            "遞延載入：9 家中 8 家僅預載 metadata、按需載入全文；OpenClaw 為唯一 eager 載入者，改以資格篩選補償。"
        ],
        font_size=7.5,
        col_widths=[0.95, 0.45, 2.25, 1.75, 1.9],
        side_by_side=True,
        row_range=(0, 5)
    )
    add_footer(s26, 26)

    s26b = prs.slides.add_slide(blank_layout)
    apply_warm_background(s26b)
    add_table_slide_adaptive(
        s26b,
        tid="S12.T10",
        title="【Table 10 解析】技能體系 (Skills) 支援、發現路徑與加載規範 (2/2)",
        category="學術表格解析",
        sub_title="Table 10: Skills Support Across Eleven Systems (Spec Conformance)",
        insights=[
            "SKILL.md 成事實標準：9/11 支援（僅 Aider、Mini-SWE 缺席）；6 家接受 `.agents/skills/`，OpenCode 還讀取 `~/.claude/skills`。",
            "YAML Frontmatter 元資料治理：透過 name、description、paths 與 requires 定義前置觸發條件。",
            "遞延載入：9 家中 8 家僅預載 metadata、按需載入全文；OpenClaw 為唯一 eager 載入者，改以資格篩選補償。"
        ],
        font_size=7.5,
        col_widths=[0.95, 0.45, 2.25, 1.75, 1.9],
        side_by_side=True,
        row_range=(5, None)
    )
    add_footer(s26b, 26)

    # -------------------------------------------------------------
    # SLIDE 27: 【Table 15 全表深度解析】Harness 與 Framework 的合流
    # -------------------------------------------------------------
    s27 = prs.slides.add_slide(blank_layout)
    apply_warm_background(s27)
    add_table_slide_adaptive(
        s27,
        tid="S14.T15",
        title="【Table 15 解析】Harness 與 Framework 的歷史性雙向合流",
        category="學術表格解析",
        sub_title="Table 15: The Harness-Framework Merger: Named, Versioned, Installable Artifacts",
        insights=[
            "雙向奔赴趨勢：Harness 廠商推出 SDK (如 Claude Agent SDK、openai-codex、openhands-sdk)；框架廠商推出專屬 Harness (如 Deep Agents)。",
            "框架定義被重塑：未來的 Agent Framework 不再是空洞的鏈式封裝，而是自帶 Loop、Tools、Sandbox 的完整 Harness 軟體庫。",
            "Rec 15 推論：要開箱即用的起點，Harness SDK 就是新的框架層——問題從「用哪個框架」變成「你已在跑哪個 Harness」。"
        ],
        font_size=8.2,
        col_widths=[2.5, 3.2, 6.033],
        side_by_side=False
    )
    add_footer(s27, 27)

    # -------------------------------------------------------------
    # SLIDE 28: 缺席一：100% 拋棄通用代理框架 (Observation 13.2)
    # -------------------------------------------------------------
    s28 = prs.slides.add_slide(blank_layout)
    apply_warm_background(s28)
    add_header(s28, "缺席之一：100% 拋棄通用代理框架 (No General Frameworks)", "核心實證震撼", "11 款生產系統零採用 LangChain / LangGraph / AutoGen / CrewAI——經三倍語料擴充與三個月複查")
    add_enlarged_bullet_card(
        s28, left=0.8, top=1.75, width=5.7, height=5.2,
        title="1. 實證調查結果 (Empirical Finding)",
        items=[
            "零採用：逐一檢查依賴清單並 grep import，約 400 萬行程式碼中無 LangChain、LangGraph、AutoGen、CrewAI 等。",
            "連原廠都跳過自家框架：Google Gemini CLI 甚至完全不使用 Google 官方的 Genkit 或 ADK 框架。",
            "全員手刻迴圈：asyncio、同步 Python、Promise/async-iterator、Tokio，各以宿主語言原語打造。",
            "邊界案例：Aider /help 可選裝 llama-index 做文件 RAG；OpenCode 以 Vercel AI SDK 為底層管線（非編排框架）。"
        ],
        tag="SHOCKING FACT",
        accent_color=BRAND_TERRA
    )
    add_enlarged_bullet_card(
        s28, left=6.833, top=1.75, width=5.7, height=5.2,
        title="2. 論文歸納的原因 (Why It Matters)",
        items=[
            "抽象遮蔽：框架多層抽象遮蔽底層 prompt 與回應，難以除錯（Building Effective Agents 警告）。",
            "靜默 Prompt 損壞：Agent 直接改動真實程式碼，隱性 prompt 變形的代價過高。",
            "快取不透明：不透明的快取行為讓快取經濟性難以掌控。",
            "Schema 版本不相容：生產 Harness 複雜度預算不同，可除錯性與 prompt 透明度勝過框架重用。"
        ],
        tag="ARCHITECTURAL LESSON",
        accent_color=BRAND_SAGE
    )
    add_footer(s28, 28)

    # -------------------------------------------------------------
    # SLIDE 29: 【Table 11 全表深度解析】29 個經典架構模式編目 (1/2) (Side-by-Side)
    # -------------------------------------------------------------
    s29 = prs.slides.add_slide(blank_layout)
    apply_warm_background(s29)
    add_table_slide_adaptive(
        s29,
        tid="S13.T11",
        title="【Table 11 解析】29 項經典架構模式編目：春季 17 項經典模式 (1/2)",
        category="學術表格解析",
        sub_title="Table 11: Catalog of 29 Recurring Architectural Patterns (Part 1/2)",
        insights=[
            "模式收斂：Event Sourcing、Policy-as-Code、Prompt Caching、Polymorphic Edits、Context Forking 等被跨系統採納。",
            "從經驗走向模式：Reflection Loop、LLM Summarization、Middleware Pipeline、JIT Repo Context 皆有多系統實作。",
            "選型檢核（簡報者觀點）：這 17 項 4 月版模式可作為評估自研或採購 Agent Runtime 的檢核表。"
        ],
        font_size=7.5,
        col_widths=[1.35, 2.75, 3.2],
        side_by_side=True,
        row_range=(0, 9)
    )
    add_footer(s29, 29)

    s29b = prs.slides.add_slide(blank_layout)
    apply_warm_background(s29b)
    add_table_slide_adaptive(
        s29b,
        tid="S13.T11",
        title="【Table 11 解析】29 項經典架構模式編目：春季 17 項經典模式 (2/2)",
        category="學術表格解析",
        sub_title="Table 11: Catalog of 29 Recurring Architectural Patterns (Part 1/2, cont.)",
        insights=[
            "模式收斂：Event Sourcing、Policy-as-Code、Prompt Caching、Polymorphic Edits、Context Forking 等被跨系統採納。",
            "從經驗走向模式：Reflection Loop、LLM Summarization、Middleware Pipeline、JIT Repo Context 皆有多系統實作。",
            "選型檢核（簡報者觀點）：這 17 項 4 月版模式可作為評估自研或採購 Agent Runtime 的檢核表。"
        ],
        font_size=7.5,
        col_widths=[1.35, 2.75, 3.2],
        side_by_side=True,
        row_range=(9, None)
    )
    add_footer(s29b, 29)

    # -------------------------------------------------------------
    # SLIDE 30: 【Table 12 全表深度解析】29 個經典架構模式編目 (2/2) (Side-by-Side)
    # -------------------------------------------------------------
    s30 = prs.slides.add_slide(blank_layout)
    apply_warm_background(s30)
    add_table_slide_adaptive(
        s30,
        tid="S13.T12",
        title="【Table 12 解析】29 項經典架構模式編目 (2/2：夏季新增 12 項模式)",
        category="學術表格解析",
        sub_title="Table 12: Catalog of 29 Recurring Architectural Patterns (Part 2/2: Summer Additions)",
        insights=[
            "新增模式：Agent-Maintained Memory、Lineage Compaction、Session-Tree Version Control、Cache-Dialect Fanout、Harness Mimicry 等。",
            "外部驗證環：OpenHands /goal 以 LLM judge 審查每次執行；Hermes verify-on-stop 否決未經驗證即結束的回合。",
            "安全新模式：Syntax-Aware Command Permissioning (OpenCode)、Untrusted-Content Delimiting（不可信內容標記）。"
        ],
        font_size=7.8,
        col_widths=[1.6, 3.6, 2.1],
        side_by_side=True
    )
    add_footer(s30, 30)

    # -------------------------------------------------------------
    # SLIDE 31: 【Table 18 全表深度解析】Claude Code vs. Codex 旗艦對決 (Side-by-Side)
    # -------------------------------------------------------------
    s31 = prs.slides.add_slide(blank_layout)
    apply_warm_background(s31)
    add_table_slide_adaptive(
        s31,
        tid="A1.T18",
        title="【Table 18 解析】兩大商業旗艦對決：Claude Code vs. OpenAI Codex (1/2)",
        category="學術表格解析",
        sub_title="Table 18: Head-to-Head Pipeline Comparison: Claude Code vs. Codex CLI",
        insights=[
            "哲學差異：Claude Code (TS) 為組合-規範式：結構化階段、工具白名單、遞迴組合與快取經濟；Codex (Rust) 原為沙盒-湧現式：安全由 OS 層保證。",
            "差距收斂：Codex 逐字採用 Claude Code 的 Hook 事件名、加入 Plan 預設與 Guardian 分類器，並可匯入 Claude Code 會話與設定。",
            "剩餘差異在於安全於何處保證：Codex 靠 OS 強制隔離，Claude Code 靠分層審查；兩者在真實基準上皆表現強勁。"
        ],
        font_size=7.5,
        col_widths=[0.95, 3.15, 3.2],
        side_by_side=True,
        row_range=(0, 4)
    )
    add_footer(s31, 31)

    s31b = prs.slides.add_slide(blank_layout)
    apply_warm_background(s31b)
    add_table_slide_adaptive(
        s31b,
        tid="A1.T18",
        title="【Table 18 解析】兩大商業旗艦對決：Claude Code vs. OpenAI Codex (2/2)",
        category="學術表格解析",
        sub_title="Table 18: Head-to-Head Pipeline Comparison: Claude Code vs. Codex CLI",
        insights=[
            "哲學差異：Claude Code (TS) 為組合-規範式：結構化階段、工具白名單、遞迴組合與快取經濟；Codex (Rust) 原為沙盒-湧現式：安全由 OS 層保證。",
            "差距收斂：Codex 逐字採用 Claude Code 的 Hook 事件名、加入 Plan 預設與 Guardian 分類器，並可匯入 Claude Code 會話與設定。",
            "剩餘差異在於安全於何處保證：Codex 靠 OS 強制隔離，Claude Code 靠分層審查；兩者在真實基準上皆表現強勁。"
        ],
        font_size=7.5,
        col_widths=[0.95, 3.15, 3.2],
        side_by_side=True,
        row_range=(4, None)
    )
    add_footer(s31b, 31)

    # -------------------------------------------------------------
    # SLIDE 32: 平台化轉型論題 (The Platform Turn)
    # -------------------------------------------------------------
    s32 = prs.slides.add_slide(blank_layout)
    apply_warm_background(s32)
    add_header(s32, "平台化轉型論題：Coding Harness 從工具走向平台", "產業趨勢", "2026 上半年完成 Tool → Platform 轉向：SDK、市集、治理層與 Meta-Harness 同步出現 (Observation 12)")
    add_enlarged_bullet_card(
        s32, left=0.8, top=1.75, width=5.7, height=5.2,
        title="1. 平台化轉型三大特徵 (The Platform Turn)",
        items=[
            "Harness 即框架：迴圈、工具、記憶、設定、擴展齊備；開發者在其「內部」工作而非 import 它。",
            "跨陣營組件規範趨同：Codex 採納 Claude Code 的 Hook 命名；OpenHands 原生支援 Claude Code 外掛。",
            "政策由 Prompt 遷移至配置：Codex 以 feature flag 取代禁 commit 規則；Vibe 改用七層優先序契約。",
            "平台經濟：Skills 9/11 領先 MCP 8/11；插件市集、跨廠會話匯入器與 MDM 治理層出現。"
        ],
        tag="PLATFORM ERA",
        accent_color=BRAND_SAGE
    )
    add_enlarged_bullet_card(
        s32, left=6.833, top=1.75, width=5.7, height=5.2,
        title="2. Databricks Omnigent：首個 Meta-Harness",
        items=[
            "Meta-Harness 崛起：押注 Harness 已成商品化元件，持久價值在上一層。",
            "統一 API 協調 11 款廠商 Harness：23 個 adapter、五種整合模式，可互為子代理（Claude 主導、Cursor 審查）。",
            "跨 Harness 政策：三層政策面 (session→agent→admin)，透過各廠 Hooks 強制執行、fail-closed。",
            "統一沙盒與出站代理（bubblewrap+seccomp / Seatbelt / Job Objects + L7 egress proxy）；以 conformance bench 測試 adapter。"
        ],
        tag="META-HARNESS",
        accent_color=BRAND_TERRA
    )
    add_footer(s32, 32)

    # -------------------------------------------------------------
    # SLIDE 33: 18 條架構實踐指南 (Recommendations 1~9)
    # -------------------------------------------------------------
    s33 = prs.slides.add_slide(blank_layout)
    apply_warm_background(s33)
    add_header(s33, "實踐者軍規 (上)：第 1 至第 9 條架構設計實踐指南", "實踐軍規", "論文 Section 16 精煉：涵蓋迴圈、模型、工具、編輯、記憶與安全防護")
    col3_w = 3.75
    add_enlarged_bullet_card(
        s33, left=0.8, top=1.75, width=col3_w, height=5.2,
        title="1. 迴圈與模型整合 (Rec 1-3)",
        items=[
            "Rec 1: 始於線性迴圈，待出現多個獨立輪次策略再演進為中間件管線。",
            "Rec 2: 自有基礎模型者緊耦合原廠並提供通用 Fallback；多模型者集中維護 per-model metadata。",
            "Rec 3: 始於單一 Bash 工具，僅在觀察到具體失敗模式時再增設微工具。"
        ],
        tag="LOOP & MODEL",
        accent_color=BRAND_SAGE
    )
    add_enlarged_bullet_card(
        s33, left=0.8 + col3_w + col3_gap, top=1.75, width=col3_w, height=5.2,
        title="2. 工具、編輯與記憶 (Rec 4-6)",
        items=[
            "Rec 4: 工具超過約 15 個時導入遞延載入（Claude Code 初始 prompt 約減 40%）。",
            "Rec 5: 根據模型等級匹配編輯合約：頂級模型採精確子字串替換，中弱模型採模糊寬容瀑布。",
            "Rec 6: 自動探索專案層級 Markdown 規格文件 (AGENTS.md, CLAUDE.md) 並相容鄰居命名。"
        ],
        tag="TOOLS & MEMORY",
        accent_color=BRAND_TERRA
    )
    add_enlarged_bullet_card(
        s33, left=0.8 + (col3_w + col3_gap)*2, top=1.75, width=col3_w, height=5.2,
        title="3. 壓縮、檢索與安全 (Rec 7-9)",
        items=[
            "Rec 7: 實作閾值邊界壓縮，保留最近完整推導尾端，增量合併摘要並相容溢位復原。",
            "Rec 8: 嚴禁對程式碼建構向量 RAG，全面改採 ripgrep、tree-sitter 與目錄走訪。",
            "Rec 9: 開發者半信任場景實作三模式審批 (PLAN / DEFAULT / YOLO) 與權限作用域。"
        ],
        tag="SECURITY & RAG",
        accent_color=BRAND_OCHRE
    )
    add_footer(s33, 33)

    # -------------------------------------------------------------
    # SLIDE 34: 18 條架構實踐指南 (Recommendations 10~18 & Anti-Patterns)
    # -------------------------------------------------------------
    s34 = prs.slides.add_slide(blank_layout)
    apply_warm_background(s34)
    add_header(s34, "實踐者軍規 (下)：第 10 至第 18 條架構指南與反模式", "實踐軍規", "論文 Section 16 精煉：涵蓋沙盒、多代理、擴展標準與四大嚴格反模式")
    add_enlarged_bullet_card(
        s34, left=0.8, top=1.75, width=col3_w, height=5.2,
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
        s34, left=0.8 + col3_w + col3_gap, top=1.75, width=col3_w, height=5.2,
        title="5. 擴展標準 (Rec 14)",
        items=[
            "Rec 14 優先級：以 SKILL.md 封裝能力範本與領域 SOP，以 MCP 整合外部程序與 API。",
            "Pi 示範可辯護的極簡立場：只用 Skills + 附 README 的 CLI 工具，不採 MCP。",
            "第三方技能套件治理：將第三方 Skill 視為依賴套件，建立信任階層、掃描與隔離機制。"
        ],
        tag="SKILLS & MCP",
        accent_color=BRAND_TERRA
    )
    add_enlarged_bullet_card(
        s34, left=0.8 + (col3_w + col3_gap)*2, top=1.75, width=col3_w, height=5.2,
        title="6. 四大嚴格反模式 (Rec 15-18)",
        items=[
            "Rec 15 禁令：嚴禁用 LangChain/AutoGen 等通用框架做 Runtime，改採原生迴圈或 Harness SDK。",
            "Rec 16 禁令：勿為程式碼建向量檢索層；若確需，先以保留任務集證明優於 ripgrep+tree-sitter。",
            "Rec 17 禁令：嚴禁將上游 SaaS API 1:1 包裝為肥大工具，應予以精煉整併。",
            "Rec 18 警戒：勿過度設計卡死偵測，但務必配置十幾行代碼的廉價計數上限保險。"
        ],
        tag="ANTI-PATTERNS",
        accent_color=BRAND_OCHRE
    )
    add_footer(s34, 34)

    # -------------------------------------------------------------
    # SLIDE 35: 附錄一：關鍵術語解析與英文縮寫對照表 (Glossary)
    # -------------------------------------------------------------
    s35 = prs.slides.add_slide(blank_layout)
    apply_warm_background(s35)
    add_header(s35, "附錄一：關鍵術語解析與英文縮寫對照表 (Glossary)", "名詞對照", "精選論文中跨 11 款系統頻繁出現之核心架構術語與標準定義")
    headers_s35 = ["術語 / 縮寫", "英文全稱", "技術意涵與在 Harness 中的核心角色"]
    rows_s35 = [
        ["Harness", "Execution Harness / Runtime", "包覆底層模型的主動執行環境，負責事件循環、工具排程、沙盒隔離與生命週期管理"],
        ["MCP", "Model Context Protocol", "連接 LLM 與外部工具、資料來源的標準協議；本研究 8/11 系統採用（Pi 明確拒絕）"],
        ["SKILL.md", "Agent Skill Specification", "agentskills.io 技能封裝規範 (Markdown+YAML)；9/11 採用，9 家中 8 家遞延載入"],
        ["ACP", "Agent Client Protocol", "Zed 系編輯器導向 JSON-RPC 協議；6/11 系統出貨，並兼作 Harness 託管介面"],
        ["Stuck Detector", "Infinite Loop / Oscillation Detector", "死循環與震盪偵測器，監控同指令反覆失敗或工具呼叫空轉，並主動介入中斷修復"],
        ["Compaction", "Threshold Compaction", "逼近上下文上限時以 LLM 摘要壓縮歷史並保留近期尾端；7/11 系統採用"],
        ["HITL", "Human-In-The-Loop", "人機協同審批機制，針對刪檔、代碼發布等高危關鍵行為強制暫停並要求人工簽核授權"],
        ["AST", "Abstract Syntax Tree", "抽象語法樹；tree-sitter 符號擷取用於確定性代碼檢索（11 系統皆不用向量檢索代碼）"],
        ["Meta-Harness", "Meta-Orchestration Runtime", "如 Databricks Omnigent，在多款原廠 Harness 之上建立的跨廠商統一治理、評測與調度層"]
    ]
    col_w_s35 = [2.0, 3.2, 6.533]
    create_table_element(slide=s35, left=0.8, top=1.75, width=11.733, height=5.2, headers=headers_s35, rows_data=rows_s35, col_widths=col_w_s35, font_size=8.5)
    add_footer(s35, 35)

    # -------------------------------------------------------------
    # SLIDE 36: 附錄二：文獻出處與研究方法論 (References & Methodology)
    # -------------------------------------------------------------
    s36 = prs.slides.add_slide(blank_layout)
    apply_warm_background(s36)
    add_header(s36, "附錄二：文獻出處、論文版本與研究方法論 (References)", "文獻溯源", "詳細標記學術論文官方出處、審查系統版本 Commit 與分析方法論")
    headers_s36 = ["類別", "項目名稱", "文獻出處 / 系統版本 Commit / 官方標註"]
    rows_s36 = [
        ["學術母篇", "arXiv:2609.00006v1", "Harness Engineering: Anatomy, Architecture, and Evolution of Coding Agents — A Source-Code Study of Eleven Systems"],
        ["作者 / 機構", "（待查證）", "本簡報所據論文全文擷取未載明作者與機構，請以 arXiv 摘要頁為準"],
        ["原廠旗艦", "Claude Code & Codex", "Claude Code (TS，2026/3 流出原始碼快照) · Codex CLI rust-v0.144.1 (vendored Bubblewrap)"],
        ["開源代表", "OpenHands & Aider", "OpenHands V1 SDK v1.34.0 (事件溯源) · Aider v0.86.3.dev (13 種編輯格式，維護模式)"],
        ["極簡代表", "Mini-SWE-Agent & Pi", "Mini-SWE-Agent v2.4.5 (~100 行) · Pi v0.80.6 (M. Zechner，極簡核心 + 擴展)"],
        ["元框架對比", "Databricks Omnigent", "Omnigent v0.4.0：Meta-Harness，於統一 API 後協調 11 款廠商 Harness (Apache 2.0)"],
        ["研究方法論", "跨系統靜態與動態審查", "原始碼閱讀（非執行量測）· 約 400 萬行三語言 · 依賴/import 掃描 · 2026/4 vs 7 快照縱向 diff"]
    ]
    col_w_s36 = [1.8, 2.5, 7.433]
    create_table_element(slide=s36, left=0.8, top=1.75, width=11.733, height=4.2, headers=headers_s36, rows_data=rows_s36, col_widths=col_w_s36, font_size=8.5)
    
    ref_card = s36.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(6.08), Inches(11.733), Inches(0.92))
    ref_card.fill.solid()
    ref_card.fill.fore_color.rgb = BG_CARD
    ref_card.line.color.rgb = BORDER_CARD
    ref_card.line.width = Pt(1)
    
    tb_ref = s36.shapes.add_textbox(Inches(1.0), Inches(6.12), Inches(11.333), Inches(0.8))
    tf_ref = tb_ref.text_frame
    tf_ref.word_wrap = True
    p_r0 = tf_ref.paragraphs[0]
    r_r0 = p_r0.add_run()
    r_r0.text = "✦ 研析方法與格式遵循宣告："
    r_r0.font.name = FONT_HEADING
    r_r0.font.size = Pt(9.5)
    r_r0.font.bold = True
    r_r0.font.color.rgb = BRAND_SAGE
    p_r1 = tf_ref.add_paragraph()
    r_r1 = p_r1.add_run()
    r_r1.text = "本簡報本於學術論文全文實證研究，完整收錄圖一、圖二、圖六之高階 Matplotlib 重繪原圖，並結合自適應排版徹底解決表格與文字重疊問題，完整納入 Table 1 至 Table 18 共 18 張學術表格與深度解讀。全面套用「pptx 樣板一」規範生成。"
    r_r1.font.name = FONT_BODY
    r_r1.font.size = Pt(8.5)
    r_r1.font.color.rgb = TEXT_MUTED
    add_footer(s36, 36)
    
    # -------------------------------------------------------------
    # SLIDE 37: 【2頁資訊圖表 · 頁面一】4K 純英文架構流程圖 (fig.png)
    # -------------------------------------------------------------
    s37 = prs.slides.add_slide(blank_layout)
    apply_warm_background(s37)
    add_header(s37, "【2頁資訊圖表 · 頁面一】Harness Engineering 4K 純英文概念架構圖", "4K 資訊圖表 (fig.png)", "Architecture & Flow Diagram: Three Main Pillars across D1-D7 Subsystems")
    
    card_37 = s37.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.75), Inches(11.733), Inches(5.2))
    card_37.fill.solid()
    card_37.fill.fore_color.rgb = BG_CARD
    card_37.line.color.rgb = BORDER_CARD
    card_37.line.width = Pt(1)
    
    fig_img = "fig.png"
    if os.path.exists(fig_img):
        # 16:9 ratio in 5.0" height gives 8.88" width
        img_h = 4.95
        img_w = 8.80
        img_left = 1.05
        s37.shapes.add_picture(fig_img, Inches(img_left), Inches(1.88), width=Inches(img_w), height=Inches(img_h))
        
        tb37 = s37.shapes.add_textbox(Inches(img_left + img_w + 0.25), Inches(1.88), Inches(11.733 - (img_w + 0.5)), Inches(img_h))
        tf37 = tb37.text_frame
        tf37.word_wrap = True
        p_t37 = tf37.paragraphs[0]
        r_t37 = p_t37.add_run()
        r_t37.text = "✦ 4K 架構圖精華導讀：\n"
        r_t37.font.name = FONT_HEADING
        r_t37.font.size = Pt(11.5)
        r_t37.font.bold = True
        r_t37.font.color.rgb = BRAND_SAGE
        
        bullets_37 = [
            "左側 Interface Layer：TUI、CLI flags、IDE protocol (ACP)、HTTP server、SDK，由人與程式驅動 Harness。",
            "Runtime Core：D1 Agent Loop（ReAct、反思迴圈、Stuck 偵測）與 D2 LLM Integration（Prompt 組裝與快取）。",
            "Tools & Memory：D3 工具（1 至 109+ 個、字串替換、ripgrep/tree-sitter）與 D4 上下文（閾值壓縮 7/11）。",
            "Governance & Scale：D5 安全（Starlark、Bubblewrap/Seatbelt）、D6 多代理（ACP/A2A）、D7 擴展（SKILL.md 9/11、MCP 8/11）。",
            "底部 Session Substrate：transcripts、persistence、resume/fork 為跨子系統共享層。"
        ]
        for b in bullets_37:
            p = tf37.add_paragraph()
            p.space_before = Pt(8)
            r = p.add_run()
            r.text = f"• {b}"
            r.font.name = FONT_BODY
            r.font.size = Pt(10)
            r.font.color.rgb = TEXT_BODY
    add_footer(s37, 37)

    # -------------------------------------------------------------
    # SLIDE 38: 【2頁資訊圖表 · 頁面二】三大維度繁中架構解析 (原生超清晰大字體卡片)
    # -------------------------------------------------------------
    s38 = prs.slides.add_slide(blank_layout)
    apply_warm_background(s38)
    add_header(s38, "【2頁資訊圖表 · 頁面二】Harness 三大維度繁中精華解析", "4K 資訊圖表精華解說", "Three Architectural Pillars & 12 Core Engineering Dimensions (arXiv:2609.00006v1)")
    
    pillars_data = [
        {
            "dim": "DIMENSION 01",
            "title": "運行時核心與驅動迴圈",
            "en": "Runtime Core & Loops (D1-D2)",
            "accent": BRAND_SLATE,
            "items": [
                ("核心等式：Agent = Model + Harness", "Harness 是模型以外的一切：迴圈、工具、上下文、安全、協調與擴展；迴圈複雜度不預測基準成績。"),
                ("D1 驅動迴圈：三大主流架構演化", "迭代迴圈 (9 系統)、Aider lint/測試反思迴圈，與 Claude Code/Codex 的協調者-工兵覆蓋層。"),
                ("D2 模型整合：Prompt 快取邊界", "原廠優化不必緊耦合，取決於誰負擔 per-provider 成本；Claude Code 以 Blake2b 切分靜態/動態快取前綴。"),
                ("死循環與失控熔斷 (Stuck Detectors)", "OpenHands 五情境 StuckDetector、Gemini CLI SHA-256+LLM 混合偵測；Claude Code、Codex 仍無自動偵測。")
            ]
        },
        {
            "dim": "DIMENSION 02",
            "title": "動作工具與記憶上下文",
            "en": "Tools, Action & Memory (D3-D4)",
            "accent": BRAND_SAGE,
            "items": [
                ("D3 工具系統：從單一 bash 起步", "工具數從 1 個 bash 到 109+；Claude Code 43 個、Pi 預設僅暴露 4 個；只在失敗模式出現時加工具。"),
                ("編輯合約依模型分級", "Frontier 模型用精確唯一子字串；開放模型用模糊瀑布 (OpenCode 九階、Lev. 0.65)；勿用行號。"),
                ("D4 記憶：閾值壓縮與持久記憶", "7/11 採閾值壓縮：Claude Code 13K 緩衝觸發；Gemini CLI 達 50% 時保留最近 30%；持久記憶成新前沿。"),
                ("雙重缺席：零框架、零代碼 RAG", "約 400 萬行、11 系統：0 個用 Agentic Framework、0 個以向量檢索代碼；改用 ripgrep / tree-sitter / glob。")
            ]
        },
        {
            "dim": "DIMENSION 03",
            "title": "安全防禦、多代理與擴展",
            "en": "Governance, Scale & Extensibility (D5-D7)",
            "accent": BRAND_TERRA,
            "items": [
                ("D5 安全體系：多層防護與沙盒", "Codex 四層：Starlark 策略、Hooks、Guardian LLM 審查、原生 OS 沙盒；Hermes 證明沙盒是選擇而非規模必然。"),
                ("D6 多代理：六種協同模式", "9/11 支援多代理；Codex 線程樹、Claude Code 遞迴組合並共享 prompt cache；子代理協同 8/9 在行程內。"),
                ("D7 擴展雙標準：SKILL.md 與 MCP", "Skills 9/11 已超越 MCP 8/11；9 家中 8 家遞延載入，並出現註冊表、信任分級與 Agent 自撰技能。"),
                ("平台化轉向：從工具到平台", "SDK 化、插件市集、跨廠匯入器、MDM 治理與 Meta-Harness 同時出現，競爭單位從迴圈轉向生態。")
            ]
        }
    ]
    
    col_w = 3.75
    col_gap = 0.24
    card_h = 5.20
    
    for i, p_info in enumerate(pillars_data):
        cx = 0.8 + i * (col_w + col_gap)
        accent = p_info["accent"]
        
        # Outer Card
        card = s38.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(cx), Inches(1.75), Inches(col_w), Inches(card_h))
        card.fill.solid()
        card.fill.fore_color.rgb = BG_CARD
        card.line.color.rgb = BORDER_CARD
        card.line.width = Pt(1)
        
        # Top Accent Header Strip
        strip = s38.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(cx + 0.12), Inches(1.85), Inches(col_w - 0.24), Inches(0.85))
        strip.fill.solid()
        strip.fill.fore_color.rgb = RGBColor(0xEA, 0xF0, 0xEC) if accent == BRAND_SAGE else (RGBColor(0xF5, 0xEB, 0xE6) if accent == BRAND_TERRA else RGBColor(0xEB, 0xEE, 0xF2))
        strip.line.color.rgb = accent
        strip.line.width = Pt(1)
        
        tf_s = strip.text_frame
        tf_s.word_wrap = True
        p_tag = tf_s.paragraphs[0]
        r_tag = p_tag.add_run()
        r_tag.text = f"✦ {p_info['dim']}  |  {p_info['en']}\n"
        r_tag.font.name = FONT_BODY
        r_tag.font.size = Pt(8.5)
        r_tag.font.bold = True
        r_tag.font.color.rgb = accent
        
        p_tit = tf_s.add_paragraph()
        r_tit = p_tit.add_run()
        r_tit.text = p_info["title"]
        r_tit.font.name = FONT_HEADING
        r_tit.font.size = Pt(12)
        r_tit.font.bold = True
        r_tit.font.color.rgb = TEXT_HEADLINE
        
        # Items Textbox
        tb_items = s38.shapes.add_textbox(Inches(cx + 0.12), Inches(2.78), Inches(col_w - 0.24), Inches(4.08))
        tf_it = tb_items.text_frame
        tf_it.word_wrap = True
        
        for idx, (it_title, it_desc) in enumerate(p_info["items"]):
            p_i_tit = tf_it.paragraphs[0] if idx == 0 else tf_it.add_paragraph()
            if idx > 0:
                p_i_tit.space_before = Pt(8)
            r_it_t = p_i_tit.add_run()
            r_it_t.text = f"• {it_title}"
            r_it_t.font.name = FONT_HEADING
            r_it_t.font.size = Pt(10.5)
            r_it_t.font.bold = True
            r_it_t.font.color.rgb = accent
            
            p_i_desc = tf_it.add_paragraph()
            p_i_desc.space_before = Pt(2)
            r_it_d = p_i_desc.add_run()
            r_it_d.text = it_desc
            r_it_d.font.name = FONT_BODY
            r_it_d.font.size = Pt(9.5)
            r_it_d.font.color.rgb = TEXT_BODY
            
    add_footer(s38, 38)
    
    out_dir = r"d:\JavaDO\執行框架"
    out_name = "Harness Engineering 論文解析.pptx"
    out_path = os.path.join(out_dir, out_name)
    prs.save(out_path)
    print(f"Successfully generated all {TOTAL_SLIDES} slides to: {out_path}")

if __name__ == "__main__":
    generate_entire_deck()
