# 實體隔離環境權威文獻深度檢索：CISA、NIST、MITRE ATLAS 與 DARPA 複合系統

> **來源主題**：公信力權威文獻檢索、五眼聯盟指引、DARPA 挑戰賽、複合 AI 系統  
> **關聯核心**：[[02_實體隔離與地端模型落地方針]] · [[06_OWASP_AISVS_1.0_評測矩陣與三大落地工程卡點]]

---

## 1. 權威治理標準（打破實體隔離迷思）

### 1.1 CISA & NSA / Five Eyes 聯合指引 (2025)
* **核心文獻**：《Careful Adoption of Agentic AI Services》
* **核心洞察**：**Air-Gap Fallacy（實體隔離迷思）**。
  - 傳統觀點認為「只要斷網就絕對安全」，但當 AI 具備自主呼叫內部工具（Tool-use）的能力時，隔離內的 Agent 便成為潛在的內部橫向移動節點。
  - 防禦關鍵由傳統網路「邊界過濾（Perimeter Defense）」轉向 **Runtime Governance（運行時治理）** 與最小工具權限（Least Privilege）。

### 1.2 NIST AI RMF 1.0 & DoD IL5/IL6 邊界標準 (2024)
* **MAP / MEASURE / MANAGE**：
  - DoD 要求隔離環境 AI 達成全生命週期邊界合規。
  - 數據入庫與模型權重必須具備數位簽章與不可篡改追溯（Tamper-Evident）。
  - 以私有 50 題黃金評估集（Evals）持續進行回歸測試，取代主觀盲目信任。

### 1.3 MITRE ATLAS（AI 威脅矩陣實踐，2024–2025）
* 針對 Agentic AI 擴展之專屬 TTPs 威脅向量：
  - **AML.T0051 工具濫用**：透過 Prompt 誘使 Agent 執行未授權系統動作。
  - **AML.T0054 記憶庫污染**：向長期記憶注入誤導性經驗導致後續決策崩潰。
* 離線環境防禦關鍵：在 **Pre-Tool 階段** 進行確定性語法與參數檢驗，而非依賴即時聯網更新的特徵庫。

---

## 2. 科研範式轉移：從單體模型走向「複合 AI 系統」

### 2.1 DARPA AIxCC (2024–2025) & TRACTOR (2024) 專案實證
* **AI Cyber Challenge (AIxCC)**：在自主修補軟體漏洞競賽中，大模型生成的修補代碼極易引入新漏洞。
* **TRACTOR 專案**：在 C 轉 Rust 的大型代碼遷移任務中，單體微調模型無法保證記憶體安全性與語意等價。
* **實證結論**：**勝負關鍵不在模型參數量大小，而在於「編譯器回饋循環、AST 靜態語法校驗、自動化測試驅動」的 Harness 編排完備度。**

### 2.2 UC Berkeley 複合 AI 系統 (Compound AI Systems, Zaharia et al. 2024)
* 現代最優解已不再是「訓練極限大單體模型」，而是由 **地端開源模型（Gemma 31B）+ RAG 檢索器 + 代碼解譯器 + Hooks 驗證器** 構成的複合確定性系統。
* 投資持久的 MCP 工具鏈、狀態機與評估集，才是抗貶值的核心資產。

### 2.3 神經 + 符號結合（Neuro-Symbolic）
* **神經端（LLM）**：負責非結構化語意理解、候選方案生成。
* **符號端（Symbolic）**：負責專家規則、MIL-STD 工程標準、CAE 邊界條件硬約束。
* 兩者結合使 31B 模型在專業領域達到 99%+ 任務通過率。

---

## 3. 核心結論

> [!IMPORTANT]
> **「Air-gap is a perimeter, not a security control.」**  
> 實體隔離僅隔絕外網攻擊；內生安全必須仰賴 Harness 最小授權、AST 代碼沙箱與不可篡改審計。
