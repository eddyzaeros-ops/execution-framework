# 第二大腦級記憶架構：Context Engineering、Git 版本管控與雙向鏈結

> **來源主題**：長期記憶設計、上下文工程、防範 Context Rot、人機共筆知識庫  
> **關聯核心**：[[01_專業領域AI解決方案評估_四種主流技術路線深層對比]] · [[02_實體隔離與地端模型落地方針]]

---

## 1. 傳統向量記憶的缺陷（Vector DB 黑盒問題）

許多 AI 團隊初期習慣將所有記憶轉為向量塞入 Vector DB，但在實戰中面臨三大災難：
1. **難以刪改與回滾**：Agent 一旦吸收了錯誤經驗，向量空間無法「精準刪除單一觀點」，導致錯誤自我複製。
2. **缺乏版本控制**：無法追蹤記憶是由哪一次執行、哪位研究員修改。
3. **Context Rot（上下文衰減）**：開機時載入過多無關記憶，耗盡有限 Context Window，大幅拉低 31B 模型的推理精準度。

---

## 2. 第二大腦三大支柱架構

### 支柱 1：Context Engineering 動態喚醒
* **極簡開機**：System Prompt 保持絕對精煉，杜絕記憶灌水。
* **按需即時檢索**：任務進行到具體步驟時，依當前意圖只將**「關聯度最高之 3 則關鍵案例與避坑指南」**注入 Context。
* **步驟結束即壓縮**：子任務完成後，動態總結執行結果並自 Context 釋放，保持乾淨推理環境。

### 支柱 2：Git-Backed 記憶版本管控
* **全純文字存儲**：全部記憶一律為純文字 Markdown 格式，存放於私有本機 Git Repository。
* **Commit 綁定 Trace**：每次任務經驗沉澱視為一次 Git Commit，嚴格綁定系統日誌之 `Trace ID`。
* **Pull Request（PR）驗收閘門**：候選記憶（Candidate Memory）發起 PR，經資深領域專家審核 Diff 後合併；若輸出偏離隨時可透過 `git revert` 達成行級精準回滾。

### 支柱 3：Obsidian 雙向鏈結思維圖譜
* **[[Wikilinks]] 語義網絡**：在決策節點、失敗教訓、特定料號與公式間建立雙向鏈結，賦予 Agent 跨專案的「非線性聯想跳轉能力」。
* **人類視覺化監控**：研發團隊直接打開 Obsidian **Graph View（圖譜檢視）**，視覺化查閱 Agent 沉澱之知識拓撲結構。

---

## 3. 記憶目錄劃分與注入策略

| 目錄結構 (Git Repo) | 核心用途 (Obsidian Vault) | Context Engineering 注入策略 | 專家治理與防禦機制 |
| :--- | :--- | :--- | :--- |
| **`/skills/`** (Procedural) | 標準排錯 SOP、代碼工程規範 | 依任務意圖動態載入對應 Skill 檔案 | 版本嚴格標記，變更需經 PR 驗收 |
| **`/episodes/`** (Episodic) | 重大專案推理思維與決策過程 | 檢索最相似之成功 Trace 摘要注入 | 帶 Trace ID 與評估分數，過期歸檔 |
| **`/anti_patterns/`** (Negative) | 踩過的坑、嚴禁使用之參數 | Pre-Tool 階段比對，觸發紅線強制中斷 | 專家直接在 Obsidian 人工補充批註 |

---

## 4. 核心架構格言

> [!NOTE]
> **「Text-based, Git-tracked, Graph-linked.」**  
> 拒絕不可讀的向量黑盒：以純文字與雙向鏈結為底座，讓 Agent 的思維記憶成為組織永續傳承的第二大腦。
