# ---------- A 專家觀點 ----------
s = d.new("重量級專家的共識：簡單架構、工程化上下文、評估先行", "專家觀點",
          "以下為原文引述與公開數據，出處見最後一頁參考資料")
EXP = [
    ("Anthropic", "“The most successful implementations use simple, composable patterns rather than complex frameworks.”",
     "→ 先固定流程，必要時才升級為自主 Agent"),
    ("Rich Sutton", "“General methods that leverage computation are ultimately the most effective, and by a large margin.”",
     "→ 手工特化模型會被通用模型追上"),
    ("Andrej Karpathy", "“Context engineering is the delicate art and science of filling the context window with just the right information for the next step.”",
     "→ 競爭力在上下文工程（檢索/工具/記憶），不在模型微調"),
    ("Andrew Ng (AI Ascent)", "HumanEval 程式測試：GPT-3.5 零樣本 48.1%、GPT-4 零樣本 67.0%；GPT-3.5 加上反思/迭代 Agent 流程躍升至 95.1%",
     "→ 架構與循環流程（Agentic Workflow）的收益超越換代大模型"),
]
cw, cg, ch = 5.8, 0.133, 1.95
for i, (who, q, so) in enumerate(EXP):
    x = 0.8 + (i % 2) * (cw + cg)
    y = 1.85 + (i // 2) * (ch + 0.15)
    card(s, x, y, cw, ch, who, [q, [(so, {"bold": True, "color": TERRA})]],
         n=i + 1, color=SAGE if i % 2 == 0 else TERRA, size=12.5, title_size=15)
quote(s, 6.0, "Simple, measured, context-first.",
      "四位專家的共識，正好對應本報告主張：Agent 主軸、評估先行、資產在上下文", h=0.95)

# ---------- A-Plus 專家共識白話解讀與落地體系 ----------
s = d.new("四大專家共識白話解讀：用最簡單的話，講透落地本質", "觀點解構",
          "將看似深奧的學術名詞，轉化為一線工程師與決策主管能立即執行的操作準則")
s.shapes.add_picture("expert_consensus_chart.png", Inches(0.8), Inches(1.85), width=Inches(6.0))

card(s, 7.05, 1.85, 5.48, 4.25, "通俗解讀：從理論到產線", [
    ("● 算力課（Rich Sutton）：", {"bold": True, "color": SLATE}),
    "不要用幾十個人的小團隊，去賭自己微調的模型能贏過數萬張 H100 訓出的通用模型；借力算力才是正道。",
    ("● 上下文工程（Andrej Karpathy）：", {"bold": True, "color": TERRA}),
    "模型不是記憶體，不要把整本百萬字規格書硬塞給它。重點在於『下一動要用什麼，就精準餵給它什麼』。",
    ("● 迭代迴圈（Andrew Ng）：", {"bold": True, "color": TERRA}),
    "聰明人一次寫完也會有疏漏。讓模型具備『寫完代碼跑跑看、錯了自己看錯誤訊息改』的迴圈，小模型也能打敗大模型。",
    ("● 極簡設計（Anthropic）：", {"bold": True, "color": SAGE}),
    "別一開始就用複雜的黑盒框架搞十幾個 Agent 聊天。能用三行固定代碼解決的，就絕不要交給模型自由發揮。"
], tag="EXPLANATION", color=TERRA, size=11, title_size=13.5)

quote(s, 6.2, "Think simple, engineer context, embrace loops.",
      "不被流行術語迷惑：掌握算力規律、做好上下文餵食、給予反思迴圈，AI 就能在專業產線穩定工作", h=0.75)

# ---------- B 上下文工程 ----------
s = d.new("上下文工程：注意力是有限預算，越多不等於越好", "核心技術",
          "Anthropic：找出「最小的高訊號 token 集合」，最大化期望結果")
CE = [["Context rot", "上下文越長，模型召回準確度越低（Anthropic 引用 needle-in-a-haystack 研究）", "不要把整份手冊塞進 prompt"],
      ["Just-in-time 檢索", "只放檔案路徑、查詢入口，由 Agent 執行時再載入", "RAG 變成工具，而非前置灌入"],
      ["壓縮 Compaction", "長任務接近上限時摘要歷史、保留決策與未解問題", "保住長流程的連貫性"],
      ["結構化筆記", "Agent 把進度寫到外部記憶，下次再讀回", "對應本報告的記憶寫入關卡"],
      ["子 Agent 分工", "子 Agent 在乾淨上下文深挖，只回傳精簡結論", "主 Agent 上下文保持乾淨"]]
table(s, 0.8, 1.9, 11.733, ["技術", "做法", "對專業領域的意義"], CE,
      [2.6, 5.6, 3.533], row_h=0.6, size=13, hl_col=2,
      aligns=[PP_ALIGN.LEFT, PP_ALIGN.LEFT, PP_ALIGN.LEFT])
quote(s, 5.85, "Fine-tuning or Retrieval? — RAG consistently outperforms.",
      "Ovadia 等（Microsoft, 2023）：知識注入上 RAG 一致優於非監督微調，模型也難以透過微調學會新事實", h=0.98)

# ---------- C Agent 評估方法 ----------
s = d.new("Agent 評估要看整條軌跡，不只看最後答案", "評估方法",
          "Hamel Husain〈Your AI Product Needs Evals〉：評估系統是 AI 產品能否持續改進的關鍵")
EV = [("L1 單元斷言", "格式、工具參數、禁用詞等可程式化檢查；每次提交都跑", SAGE),
      ("L2 軌跡審查", "人工 + LLM 評審檢視完整 trace：選對工具？步驟多餘？有無幻覺？", TERRA),
      ("L3 結果驗收", "專家依評估集打分，或由業務指標（節省工時、正確率）驗證", SAGE)]
for i, (t_, b_, c_) in enumerate(EV):
    card(s, 0.8 + i * 3.992, 1.9, 3.75, 2.2, t_, [b_], n=i + 1, color=c_, size=13.5, title_size=16)
NOTE = [["LLM 評審需校準", "先與專家標註比對一致率，再放手自動評分"],
        ["先看資料再寫指標", "從真實失敗 trace 歸納錯誤類型，而非憑空設計"],
        ["評估集要版本化", "換模型、換 prompt、蒸餾前後都用同一份比較"]]
table(s, 0.8, 4.35, 11.733, ["原則", "做法"], NOTE, [3.4, 8.333], row_h=0.62, size=13.5,
      aligns=[PP_ALIGN.LEFT, PP_ALIGN.LEFT])

# ---------- D 安全 ----------
s = d.new("Agent 安全：三個條件同時成立，資料就可能外洩", "安全治理",
          "Simon Willison「Lethal Trifecta」：私有資料 + 不可信內容 + 對外通訊")
TRI = [("存取私有資料", "內部文件、資料庫、郵件", SAGE),
       ("接觸不可信內容", "外部文件、網頁、來文附件可夾帶提示注入", TERRA),
       ("能對外通訊", "HTTP 請求、圖片連結、寄信都可能成為外洩管道", SAGE)]
for i, (t_, b_, c_) in enumerate(TRI):
    card(s, 0.8 + i * 3.992, 1.9, 3.75, 1.75, t_, [b_], n=i + 1, color=c_, size=13.5, title_size=16)
SEC = [["切斷任一條件", "內網隔離即切斷「對外通訊」，是地端部署的天然優勢"],
       ["工具最小權限", "唯讀優先；寫入、刪除、發送類工具一律人工核准"],
       ["全程稽核", "每次工具呼叫留存參數、結果與使用者身分"],
       ["標準化工具介面", "以 MCP 等開放協定統一包裝，集中做權限與審計"]]
table(s, 0.8, 3.9, 11.733, ["對策", "做法"], SEC, [3.4, 8.333], row_h=0.6, size=13.5,
      aligns=[PP_ALIGN.LEFT, PP_ALIGN.LEFT])


