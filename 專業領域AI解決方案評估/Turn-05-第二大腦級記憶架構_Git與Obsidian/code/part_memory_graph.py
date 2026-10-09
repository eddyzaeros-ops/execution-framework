# ---------- 11-Plus 第二大腦級記憶架構 ----------
s = d.new("第二大腦級記憶：Context Engineering、Git 版本管控與雙向鏈結", "記憶進階架構",
          "在有限的 Context 預算內，以純文字、雙向鏈結與 Git 打造人機共筆的永續資產")

MEM_PILLARS = [
    ("1. Context Engineering 動態喚醒", "記憶不是開機全載入。平時 System Prompt 保持極簡（避免 Context Rot）；任務進行時按需檢索，只將『當前步驟相關之 3 則關鍵案例與避坑指南』注入 Context，步驟結束即壓縮釋放。"),
    ("2. Git-Backed 記憶版本管控", "全庫採用純文字 Markdown 存放於內網私有 Git。每次經驗沉澱等於一次 commit，附帶 Trace ID；候選記憶發起 PR 由專家審核 Diff 後合併，若輸出偏差可隨時 git revert 行級回滾。"),
    ("3. Obsidian 雙向鏈結思維圖譜", "利用 [[Wikilinks]] 將專案決策、呼叫工具、失敗教訓與專家批註彼此鏈結；Agent 具備『聯想跳轉能力』，人類研發團隊亦可直接打開 Obsidian Graph View 視覺化監控知識網絡。")
]

cw, cg = 3.75, 0.242
for i, (mtitle, mdesc) in enumerate(MEM_PILLARS):
    x = 0.8 + i * (cw + cg)
    card(s, x, 1.72, cw, 2.38, mtitle, [mdesc], n=i + 1, color=SAGE if i % 2 == 0 else TERRA, size=11, title_size=13)

MEM_TABLE = [
    ["目錄結構 (Git Repo)", "核心用途 (Obsidian Vault)", "Context Engineering 注入策略", "專家治理與防禦機制"],
    ["/skills/ (Procedural)", "標準排錯 SOP、代碼工程規範", "依任務意圖動態載入對應 Skill 檔案", "版本嚴格標記，變更需經 PR 驗收"],
    ["/episodes/ (Episodic)", "重大專案推理思維與決策過程", "檢索最相似之成功 Trace 摘要注入", "帶 Trace ID 與評估分數，過期歸檔"],
    ["/anti_patterns/ (Negative)", "踩過的坑、嚴禁使用之參數", "Pre-Tool 階段比對，觸發紅線強制中斷", "專家直接在 Obsidian 人工補充批註"]
]

table(s, 0.8, 4.25, 11.733, MEM_TABLE[0], MEM_TABLE[1:],
      [2.5, 3.2, 3.2, 2.833], row_h=0.42, size=10.5, hl_col=0,
      aligns=[PP_ALIGN.LEFT, PP_ALIGN.LEFT, PP_ALIGN.LEFT, PP_ALIGN.LEFT])

quote(s, 6.20, "Text-based, Git-tracked, Graph-linked.",
      "拒絕不可讀的向量黑盒：以純文字與雙向鏈結為底座，讓 Agent 的思維記憶成為組織永續傳承的第二大腦", h=0.6)
