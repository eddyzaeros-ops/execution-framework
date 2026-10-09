import re

def reorder_and_enhance():
    with open('generate_full_deck.py', 'r', encoding='utf-8') as f:
        text = f.read()

    # Step 1: Update add_matplotlib_figure_slide to ensure zero overlap
    old_aspect_logic = """        if aspect > 1.85:
            # Wide diagram: Top picture (height ~2.8"), Bottom commentary
            img_top = 1.90
            img_w = 11.3
            img_h = min(2.85, img_w / aspect)
            img_left = 0.8 + (11.733 - img_w) / 2
            slide.shapes.add_picture(fig_img_path, Inches(img_left), Inches(img_top), width=Inches(img_w), height=Inches(img_h))
            
            # Bottom text box
            tb = slide.shapes.add_textbox(Inches(1.1), Inches(4.88), Inches(11.133), Inches(2.0))
            tf = tb.text_frame
            tf.word_wrap = True
            
            p_cap = tf.paragraphs[0]
            r_c = p_cap.add_run()
            r_c.text = f"✦ 論文官方題註 (Caption)：{original_caption}"
            r_c.font.name = FONT_HEADING
            r_c.font.size = Pt(10.5)
            r_c.font.bold = True
            r_c.font.color.rgb = BRAND_TERRA
            
            for ins in insights:
                p = tf.add_paragraph()
                p.space_before = Pt(4)
                r = p.add_run()
                r.text = f"• {ins}"
                r.font.name = FONT_BODY
                r.font.size = Pt(10.5)
                r.font.color.rgb = TEXT_BODY"""

    new_aspect_logic = """        if aspect > 1.85:
            # Wide diagram: Top picture (height ~2.45"), Bottom commentary (top 4.45", height 2.45")
            # Completely eliminates any vertical collision or overlap!
            img_top = 1.85
            img_w = 10.8
            img_h = min(2.45, img_w / aspect)
            img_left = 0.8 + (11.733 - img_w) / 2
            slide.shapes.add_picture(fig_img_path, Inches(img_left), Inches(img_top), width=Inches(img_w), height=Inches(img_h))
            
            # Bottom text box
            tb = slide.shapes.add_textbox(Inches(1.1), Inches(4.45), Inches(11.133), Inches(2.45))
            tf = tb.text_frame
            tf.word_wrap = True
            
            p_cap = tf.paragraphs[0]
            r_c = p_cap.add_run()
            r_c.text = f"✦ 論文官方題註 (Caption)：{original_caption}"
            r_c.font.name = FONT_HEADING
            r_c.font.size = Pt(10.5)
            r_c.font.bold = True
            r_c.font.color.rgb = BRAND_TERRA
            
            for ins in insights:
                p = tf.add_paragraph()
                p.space_before = Pt(3)
                r = p.add_run()
                r.text = f"• {ins}"
                r.font.name = FONT_BODY
                r.font.size = Pt(10)
                r.font.color.rgb = TEXT_BODY"""

    if old_aspect_logic in text:
        text = text.replace(old_aspect_logic, new_aspect_logic)
        print("Updated add_matplotlib_figure_slide aspect layout successfully.")
    else:
        print("Warning: old_aspect_logic not found exactly.")

    # Step 2: Extract slide blocks
    indices = [m.start() for m in re.finditer(r'    # SLIDE \d+:', text)]
    indices.append(text.find('    out_dir =', indices[-1]))

    slides_dict = {}
    for i in range(len(indices) - 1):
        chunk = text[indices[i]:indices[i+1]]
        num = int(re.search(r'    # SLIDE (\d+):', chunk).group(1))
        slides_dict[num] = chunk

    # Step 3: Enhance Slide 4 with AI-ROS definition
    s4_chunk = slides_dict[4]
    s4_old_ins = """        insights=[
            "原圖核心拓撲：精準呈現以 Agent Loop (D1) 為心臟的向心結構，所有外部交互均被嚴格限制在 Runtime 內部。",
            "橫切面 (Cross-cutting Surfaces)：介面層 (TUI/IDE/SDK/Server) 與會話基底 (Session Substrate - 軌跡/持久化/分支) 貫穿七大子系統。",
            "論文作者核心結論：每一款系統，哪怕小至 100 行的 Mini-SWE-Agent，都必須對這七大子系統做出明確架構表態（哪怕表態為留白）。"
        ]"""

    s4_new_ins = """        insights=[
            "【圖中核心術語：什麼是 AI-ROS？】AI 運行時操作系統 (AI Runtime Operating System)。論文核心論斷指出：Coding Harness 已超越簡單腳本，演化為承擔進程管理、權限沙盒、工具調度、記憶持久化與死循環熔斷的智慧體作業系統底座，為無狀態 LLM 賦予可預測的確定性軟體工程實踐能力。",
            "向心解剖學架構：精準呈現以 Agent Loop (D1) 為心臟的向心閉環，向外輻射調度模型 (D2)、工具 (D3)、記憶 (D4)、安全 (D5)、多代理 (D6) 與擴展 (D7)。",
            "雙大貫穿基底：介面層 (TUI/IDE/SDK/Server) 與會話基底 (Session Substrate 軌跡持久化與分支樹) 橫切貫穿所有子系統。"
        ]"""

    if s4_old_ins in s4_chunk:
        slides_dict[4] = s4_chunk.replace(s4_old_ins, s4_new_ins)
        print("Updated Slide 4 with comprehensive AI-ROS definition!")
    else:
        print("Warning: s4_old_ins not found in Slide 4.")

    # Step 4: Reorder slides according to logical narrative
    new_order = [
        1, 2, 13, 14,      # Chap 1: 背景、定義與生態全貌 (Cover, Thesis, Table 2, Table 3)
        3, 4, 12, 15,      # Chap 2: 解剖學架構 (Fig 1 Overview, Fig 1 Redraw, Table 1, Table 4)
        5, 6, 16,          # Chap 3: 驅動迴圈 (Fig 2 Overview, Fig 2 Redraw, Table 5)
        17, 27, 28,        # Chap 4: 模型整合 (Table 6, Table 16, Table 17)
        18, 19, 24, 31,    # Chap 5: 動作工具與沙盒 (Table 7, Table 8, Table 13, Observation RAG)
        9,                 # Chap 6: 記憶上下文 (Fig 4 Strategies)
        10,                # Chap 7: 安全防禦 (Fig 5 Claude vs Codex)
        7, 8, 11, 20, 25,  # Chap 8: 多代理拓撲 (Fig 6 Overview, Fig 6 Redraw, Fig 7 Stages, Table 9, Table 14)
        21, 26, 30,        # Chap 9: 擴展標準與趨勢 (Table 10, Table 15, Observation Frameworks)
        22, 23, 29, 32,    # Chap 10: 29模式與對決 (Table 11, Table 12, Table 18, Platform Turn)
        33, 34,            # Chap 11: 18條實踐軍規 (Rec 1-9, Rec 10-18)
        35, 36, 37, 38     # Chap 12: 附錄與資訊圖表 (Glossary, References, 4K fig.png, 4K doc.png)
    ]

    header_code = text[:indices[0]]
    footer_code = text[indices[-1]:]

    reconstructed_body = []
    for new_idx, old_num in enumerate(new_order, start=1):
        chunk = slides_dict[old_num]
        
        # Update Slide header comment
        chunk = re.sub(r'    # SLIDE \d+:', f'    # SLIDE {new_idx}:', chunk, count=1)
        
        # Replace variable sX with s{new_idx}
        var_name_match = re.search(r'    (s\d+) = prs\.slides\.add_slide\(blank_layout\)', chunk)
        if var_name_match:
            old_var = var_name_match.group(1)
            new_var = f"s{new_idx}"
            chunk = re.sub(r'\b' + old_var + r'\b', new_var, chunk)
            
        # Update footer page number
        chunk = re.sub(r'add_footer\(\s*\w+\s*,\s*\d+\s*\)', f'add_footer(s{new_idx}, {new_idx})', chunk)

        reconstructed_body.append(chunk)

    final_script = header_code + "".join(reconstructed_body) + footer_code

    with open('generate_full_deck.py', 'w', encoding='utf-8') as f:
        f.write(final_script)

    print("Successfully re-ordered and generated updated generate_full_deck.py!")

if __name__ == '__main__':
    reorder_and_enhance()
