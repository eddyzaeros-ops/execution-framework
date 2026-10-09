# Turn-02-SDK-Use-Cases-and-Role-Division: 業務流程 Agent vs. 程式碼開發 Agent 適用場景與角色分工

---

## 🗣️ 每輪使用者原始提問需求 (User Requests)

> **User Prompt**:
> "自動對帳 Agent、文檔問答 Agent、自動客訴處理流，不能由 Antigravity 2.0, Claude Code 進行開發嗎"

---

## 📑 文件摘要 (Document Summary)

深入對比「領域專屬業務 Agent（對帳、問答、客服）」與「專屬程式碼開發 Agent」的架構分歧。明確指出 Claude Code / Antigravity 2.0 是專精於軟體工程的端點智慧體，而業務流 Agent 則需透過 Agent SDK 深度串接企業 ERP/CRM、資料庫權限審計與自定義業務工作流。

---

## 🏷️ 版本管理 (Version Tracking)

- **正式版本號**：`v1.1.0`
- **模組狀態**：`正式收斂 (GA)`
- **治理分類**：企業級架構研析與對話模組歸檔
- **上層對話主題**：`AI-Agent-SDK與Antigravity核心架構解析`

---

## 🔄 版本差異說明 (Changelog / Diffs)

- 新增業務領域 Agent 與軟體開發 Agent 之職責分離評估模型。
- 分析企業地端自建 Agent 與終端 Pair Programmer 之混合架構拓撲。

---

## 📂 子目錄資產清單 (Sub-Directory Assets)

- `docs/`：本模組相關之 Word 留痕報告 (`.docx`) 與 Markdown 筆記 (`.md`)
- `pptx/`：本模組對應之簡報投影片 (`.pptx`)
- `code/`：實體原始碼與自動化生成腳本 (`.py`, `.json`, `.sh`)
- `html/`：HTML 檔案與互動儀表板 (`.html`, `.htm`)
- `assets/`：4K 高解析度資訊圖表、架構圖資與視覺素材 (`.png`, `.svg`)
