# ---------- 3 實體隔離地端實戰落地方針 ----------
s = d.new("實體隔離實戰：只有 Gemma 31B，如何讓國防 AI Agent 安全落地？", "核心戰略",
          "一針見血：不搞高風險自訓，以「31B 開源權重 + 成熟 Harness + 零信任護欄」建構內網自主生態")

GUIDE_P3 = [
    ["1. 算力基座：Gemma 31B (合規核心)", "單張 A100 / RTX 4090 (Q4 量化) 即可全地端推論；Apache 2.0 協議、原生多模態與高精度指令遵循。", "擺脫外部雲端依賴，資料 100% 留在內網，杜絕外洩風險。"],
    ["2. 外殼借力：成熟 Harness (免重複造輪)", "長程排程採 DeepAgents (檔案記憶)；代碼工程採 OpenCode (規範約束)；經驗沉澱採 Hermes (提煉 Skills)。", "直接繼承全球頂尖 Agent 狀態機與記憶機制，省下數年探索時間。"],
    ["3. 領域資產：SOP 代碼化 (取代盲目微調)", "專家做事手冊化為可執行的 Skills 檔；建置混合 RAG (向量+BM25)；現有系統以 MCP 標準微服務封裝。", "微調會遺忘事實；將經驗固化為上下文與 MCP 工具，資產永遠屬於自己。"],
    ["4. 國防安全：Hooks 零信任護欄 (確保零失誤)", "Pre-Tool 參數靜態審查、代碼沙箱隔離、高敏感動作強制 Human-in-the-loop 人工核准、50 題黃金評估集日常回歸。", "用確定性代碼牢牢約束 31B 模型隨機性，達到國防級極致精準與安全。"]
]

table(s, 0.8, 1.85, 11.733, ["實戰突圍維度", "實體隔離環境的具體工程實作做法", "一針見血的國防研發價值"], GUIDE_P3,
      [2.8, 5.3, 3.633], row_h=0.72, size=11.5, hl_col=2,
      aligns=[PP_ALIGN.LEFT, PP_ALIGN.LEFT, PP_ALIGN.LEFT])

quote(s, 5.85, "Scaffolding + Rigorous Hooks = Mission-Critical Reliability.",
      "國防 AI 落地核心：智力靠合規開源 31B、流程靠成熟 Harness、安全靠 Hooks 護欄、演進靠私有評估集", h=0.95)

# ---------- 3-Plus 1 實體隔離環境運作全景 (架構圖) ----------
s_fig = d.blank()
s_fig.shapes.add_picture(r"d:\JavaDO\執行框架\fig.png", Inches(0), Inches(0), width=Inches(13.333), height=Inches(7.5))

# ---------- 3-Plus 2 實體隔離環境運作全景 (深度解析面板) ----------
s_doc = d.blank()
s_doc.shapes.add_picture(r"d:\JavaDO\執行框架\doc.png", Inches(0), Inches(0), width=Inches(13.333), height=Inches(7.5))
