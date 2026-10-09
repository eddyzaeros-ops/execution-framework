# ---------- E 地端開源模型評比 ----------
s = d.new("地端前沿開源模型選型：推論邏輯、長上下文與自主演進", "地端選型",
          "實體隔離內網無外部 API 時，依任務特化配置最新開源與開放權重架構")
MODELS = [
    ["Nemotron (NVIDIA 70B/Nano)", "RLHF/邏輯對話、高吞吐 NIM", "通用複雜對話、結構化綜合分析、合規審核", "搭配 TensorRT-LLM/NIM 部署，GPU 運算吞吐極佳"],
    ["Kimi K3 / K2.5 (Moonshot MoE)", "超長上下文 (1M)、原生多模態", "超大專業技術規範、長篇工程日誌跨篇分析", "MoE 架構需分散式顯存叢集，適合中樞級知識檢索"],
    ["Gemma 4 (Google 31B Dense)", "多模態原生整合、指令遵循極佳", "技術圖表解析、代碼輔助生成、跨模態比對", "單張高階卡 (H100/4090 Q4) 可跑，性價比極高"],
    ["Ornith-1.5 (35B MoE / 397B)", "自主強化學習閉環、Agent 導向", "多步複雜工具呼叫、動態任務鷹架規劃", "內建自我反思機制，對齊 Agentic Trace 執行流"],
    ["Qwen 2.5/3 & DeepSeek-R1", "穩定 Tool Call 與 CoT 深度推理", "底層系統 API 呼叫、精密數學運算與演算法", "開源生態支援最完整，為地端 Agent 核心基石"]
]
table(s, 0.8, 1.85, 11.733, ["模型家族與代表規格", "架構與核心優勢", "最適合之 Agent 職責", "地端隔離硬體與部署特性"], MODELS,
      [2.8, 2.5, 3.4, 3.033], row_h=0.64, size=11.5, hl_col=2,
      aligns=[PP_ALIGN.LEFT, PP_ALIGN.LEFT, PP_ALIGN.LEFT, PP_ALIGN.LEFT])
quote(s, 5.85, "Heterogeneous Deployment: Specialized models for specialized steps.",
      "地端實踐：以 Qwen/Gemma 負責高頻 Tool Call，Nemotron/R1 負責深度推論，Kimi 負責長文檔分析，兼顧延遲與精度", h=0.95)

# ---------- F 開源 Harness 框架評比 ----------
s = d.new("新世代 Agent Harness 評比：從單純框架到自主進化套件", "框架評比",
          "評估地端隔離部署時的長任務規劃、檔案沙箱、技能沉澱與控制粒度")
FRAMEWORKS = [
    ["LangChain Deep Agents", "長程規劃、檔案系統記憶、子 Agent 派工", "解決長時間運作 Context Rot；內建檔案系統做外部記憶", "基於 LangGraph 狀態機，生產環境穩定性高"],
    ["Nous Hermes Agent", "自我學習迴圈、Skills 動態提取沉澱", "執行成功後自動提煉為新 Skill 檔；具備跨會話記憶", "極契合專業領域長期積累；開箱即用支援本機部署"],
    ["OpenCode (SST)", "Terminal/CLI 原生、多 Agent 分工 (Scout/Build)", "專注代碼庫重構與系統工程；藉由 AGENTS.md 固化規則", "型別安全微服務 (Bun/TS 架構)，執行效率極高"],
    ["LangGraph / PydanticAI", "圖狀態機 (StateGraph) / 嚴格 Schema 契約", "精確控制狀態流轉、斷點回復 (Human-in-the-loop)", "提供最大底層控制權，適合極度嚴謹的核心業務介接"]
]
table(s, 0.8, 1.85, 11.733, ["Harness / 套件名稱", "核心架構機制", "關鍵優勢與 Agent 賦能亮點", "地端隔離導入與控制價值"], FRAMEWORKS,
      [2.5, 2.8, 3.6, 2.833], row_h=0.68, size=12, hl_col=0,
      aligns=[PP_ALIGN.LEFT, PP_ALIGN.LEFT, PP_ALIGN.LEFT, PP_ALIGN.LEFT])
quote(s, 5.85, "Harness = Scaffolding + Memory + Skills Accumulation.",
      "新世代 Harness（如 Hermes、Deep Agents）超越了單純的 prompt loop，自帶檔案記憶與 Skill 沉澱，直接實踐增值資產主張", h=0.95)

# ---------- G 實體隔離環境的 AI 生態系 ----------
s = d.new("實體隔離環境（Air-Gapped）：專業領域 AI 生態營造", "環境治理",
          "兼顧國防研發機密防護與 AI Agent 敏捷演進的四層工程體系")
AIRGAP = [
    ("內外網安全泵（Air-Gap Bridge）", "建立單向安全檢驗閘道：外部開源權重、安全套件與開源文獻經多重掃描/防毒後入庫，嚴禁雙向未稽核通訊。", SAGE),
    ("地端私有 Registry 與資產庫", "架設內部專用 HuggingFace Mirror、私有 PyPI 與 Docker Registry；統一納管模型權重、Skills 與 Prompt 樣板。", TERRA),
    ("容器化執行沙箱（Zero-Trust Runtime）", "Agent 工具呼叫與程式碼執行必須在嚴格隔離的沙箱容器內（無外網存取、唯讀掛載核心系統），防止惡意注入逃逸。", SAGE),
    ("Trace 軌跡中樞與私有評估網", "內網架設私有追蹤平台（如 OpenTelemetry/Phoenix），集中記錄每筆思考路徑與呼叫紀錄，供領域專家校準與回流。", TERRA)
]
cw, cg, ch = 5.8, 0.133, 1.95
for i, (title_, body_, col_) in enumerate(AIRGAP):
    x = 0.8 + (i % 2) * (cw + cg)
    y = 1.85 + (i // 2) * (ch + 0.15)
    card(s, x, y, cw, ch, title_, [body_], n=i + 1, color=col_, size=12, title_size=14)
quote(s, 6.0, "Air-gapped does not mean isolated from evolution.",
      "生態系的關鍵在於：模型可受控升級、評估集可持續積累、工具呼叫安全可溯，形成內網閉環飛輪", h=0.95)

# ---------- H Hooks 生命週期與安全攔截機制 ----------
s = d.new("Hooks 機制：Agent 生命週期的神經中樞與安全攔截點", "架構機制",
          "在 Agent 思考、工具呼叫、記憶讀寫的前中後，植入確定性的防護閥門與審計機制")
HOOKS = [
    ["Pre-Tool Execution (工具呼叫前)", "參數結構校驗、危險指令靜態掃描、權限驗證", "防止提示注入引發的非預期危險操作（如格式化、外洩私有資料）"],
    ["Post-Tool Execution (工具呼叫後)", "結果脫敏過濾、長輸出壓縮、執行結果真實性驗證", "防範輸出資料超出 context 造成 Context Rot，或錯誤資料污染記憶"],
    ["Pre-Step Planning (思考規劃前)", "動態注入組織最新安全規範、環境邊界約束、Token 預算限制", "約束模型發散思考，將注意力鎖定在合規的目標範圍內"],
    ["Memory Ingestion (記憶寫入前)", "三階段寫入關卡、去重、矛盾偵測、機密等級分類", "確保只有經人工核准或評估集驗收的高價值經驗方可永久沉澱"],
    ["Human-in-the-loop (人工審批閥)", "特定敏感動作（刪除、變更設定、資金/指令送出）暫停中斷點", "將最終裁決權牢牢保留在領域專家手中，達到零失誤容忍度"]
]
table(s, 0.8, 1.85, 11.733, ["Hook 攔截階段", "核心觸發機制與檢查內容", "對專業與國防領域的關鍵價值"], HOOKS,
      [3.0, 4.5, 4.233], row_h=0.62, size=12, hl_col=0,
      aligns=[PP_ALIGN.LEFT, PP_ALIGN.LEFT, PP_ALIGN.LEFT])
quote(s, 5.85, "Hooks: The deterministic seatbelt for non-deterministic intelligence.",
      "大模型是非確定性的，但生產系統必須是確定性的；Hooks 是把非確定性智力約束在安全軌道上的核心保險栓", h=0.95)

# ---------- I MCP 企業與研發系統整合架構 ----------
s = d.new("MCP（Model Context Protocol）：鏈結現有研發與資訊系統的通用介面", "系統整合",
          "以開放標準將 MIS、科學模擬器與內部資料庫解耦封裝為安全微服務")
MCP_LAYERS = [
    ("通用通訊協定 (Protocol Layer)", "採用開放標準 JSON-RPC 2.0，將 LLM/Agent 與後端實體系統徹底解耦；換模型無需重寫系統介接 API。", SAGE),
    ("MIS 營運與研發管理封裝", "透過 MCP Server 封裝專案管理系統、研發文檔庫、ERP/資產庫，支援唯讀查詢、狀態回報與跨庫比對。", TERRA),
    ("科學計算與工程模擬器介接", "將通用空氣動力、熱流、結構等工程模擬器封裝為 MCP 工具，Agent 自主設定參數檔、提交排程與分析輸出報告。", SAGE),
    ("網關級安全管控 (MCP Gateway)", "集中實施 RBAC 權限控管、金鑰隔離與雙向稽核紀錄，確保 Agent 僅能在授權沙箱環境內操作現有系統。", TERRA)
]
cw, cg, ch = 5.8, 0.133, 1.95
for i, (title_, body_, col_) in enumerate(MCP_LAYERS):
    x = 0.8 + (i % 2) * (cw + cg)
    y = 1.85 + (i // 2) * (ch + 0.15)
    card(s, x, y, cw, ch, title_, [body_], n=i + 1, color=col_, size=12, title_size=14)
quote(s, 6.0, "Decouple intelligence from tools via standardized protocols.",
      "MCP 的核心價值：模型隨時可換，但已封裝的 MIS 系統、工程模擬器與資料庫介面成為組織長久資產", h=0.95)


