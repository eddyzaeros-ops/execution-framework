# ==============================================================================
# 擴充頁面：
# 1. Sub-Agent 深度說明 (Why, What, How, When, Where)
# 2. 地端實戰：只有 Gemma 31B 搭配 Hermes / OpenCode / DeepAgents 落地指南
# ==============================================================================

# ---------- J Sub-Agent 5W 分析 ----------
s = d.new("Sub-Agent 體系：Why、What、How、When、Where 深度解構", "架構機制",
          "解決複雜任務中 Context Rot 與職責混雜的關鍵架構手段")
SUB_CARDS = [
    ("Why（為什麼需要？）", "單一 Agent 承擔過多工具與長歷史會造成 Context Rot，注意力分散導致幻覺與死循環。透過 Sub-Agent 將任務隔離在乾淨的上下文（Clean Context），大幅提升各子任務的執行成功率。"),
    ("What（它是什麼？）", "Sub-Agent 是主 Agent 派生出的特化子智慧體。它擁有專屬的角色提示詞（Role Prompt）、受限的最小工具集，以及獨立的執行環境，完成任務後僅向主 Agent 提交精煉結論。"),
    ("How（如何運作？）", "主 Agent 將總目標拆解為子任務（Planning）➔ 呼叫 Sub-Agent 並傳遞專屬 Context ➔ Sub-Agent 在沙箱中自主迴圈（ReAct/Code）➔ 檢驗輸出並總結 ➔ 主 Agent 吸收結果繼續推進。"),
    ("When & Where（何時/何處使用？）", "【When】當任務具備獨立探索性（如深挖代碼、長篇文檔檢索、多參數模擬計算）時啟用；【Where】部署在隔離容器沙箱或專屬微服務節點，嚴防非授權的跨環境資料外洩。")
]
cw, cg, ch = 5.8, 0.133, 2.05
for i, (title_, body_) in enumerate(SUB_CARDS):
    x = 0.8 + (i % 2) * (cw + cg)
    y = 1.85 + (i // 2) * (ch + 0.15)
    card(s, x, y, cw, ch, title_, [body_], n=i + 1, color=SAGE if i % 2 == 0 else TERRA, size=11.5, title_size=13.5)
quote(s, 6.15, "Divide and Conquer: Keep the main context immaculate.",
      "主 Agent 負責長程排程與決策，Sub-Agent 深入戰壕攻堅；乾淨的上下文是高品質輸出的第一前提", h=0.75)

