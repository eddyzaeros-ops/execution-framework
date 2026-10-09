# 專案系列對話：AI-Agent-SDK與Antigravity核心架構解析

本資料夾彙整此對話系列中所有協同研析與開發之歷史輪次、對應之使用者原始提問、各輪次文件摘要、版本收斂歷程與實體資產。

---

## 🧭 對話輪次導航矩陣 (Turn Navigation Matrix)

| 輪次代號 | 研析與模組主題 | 版本 | 核心產出物 / 資產清單 | 模組直達連結 |
| :--- | :--- | :---: | :--- | :--- |
| **Turn 01** | Agent SDK 定位、核心機制與主流生態比較 | `v1.0.0` | 三大原廠 SDK 技術規格矩陣與分層模型 | [README](file:///./Turn-01-Agent-SDK-and-Ecosystem/README.md) |
| **Turn 02** | 業務流程 Agent vs. 程式碼開發 Agent 適用場景 | `v1.1.0` | 業務流與軟體工程智慧體分工評估模型 | [README](file:///./Turn-02-SDK-Use-Cases-and-Role-Division/README.md) |
| **Turn 03** | Agent SDK 落地實現架構：記憶、MCP 與編排 | `v1.2.0` | 實體程式碼級別調用模式與四層防護架構 | [README](file:///./Turn-03-Agent-SDK-Code-Level-Implementation/README.md) |
| **Turn 04** | VS Code + SDK vs. Antigravity 2.0 工作流比較 | `v1.3.0` | 十維度開發者工作流對比與選型決策樹 | [README](file:///./Turn-04-VS-Code-vs-Antigravity-2.0-Workflow/README.md) |
| **Turn 05** | Antigravity IDE、核心引擎與 VS Code 架構解析 | `v1.4.0` | IDE 面板、協同引擎與編輯器三維架構解構 | [README](file:///./Turn-05-Antigravity-IDE-vs-VS-Code-and-Engine/README.md) |
| **Turn 06-07** | AI Agent 原廠生態系 4K 資訊圖表設計 | `v1.5.0` | `generate_final_infographic.py`, `AI_Agent_Ecosystem_Architecture_4K.png` | [README](file:///./Turn-06-to-07-AI-Agent-Ecosystem-Infographic/README.md) |
| **Turn 08-09** | 4K 雙頁式視覺系統 (fig.png + doc.png) | `v1.6.0` | `split_infographic.py`, `generate_fullscreen_images.py`, `fig.png`, `doc.png` | [README](file:///./Turn-08-to-09-Split-and-Fullscreen-4K-Infographics/README.md) |
| **Turn 10** | 全域標準技能建立：2 頁資訊圖表 | `v1.7.0` | `2-page-infographic` 全域 Skill 規範與實施標準指南 | [README](file:///./Turn-10-Global-Skill-2-Page-Infographic/README.md) |
| **Turn 11** | 工具比較 4K 雙頁圖資實裝產出 | `v1.8.0` | `generate_agy2_images.py`, `fig_agy2.png`, `doc_agy2.png` | [README](file:///./Turn-11-Tool-Comparison-4K-Infographics/README.md) |
| **Turn 12-17** | 專案對話管理治理：獨立 Repo 建立與全域技能迭代 | `v2.0.0` | 獨立專屬 Repo 治理、頂層對話目錄封裝、使用者原始提問留痕 | [README](file:///./Turn-12-to-17-Dedicated-Repo-Governance/README.md) |

---

## 🏛️ 模組化目錄結構

```text
AI-Agent-SDK與Antigravity核心架構解析/
├── README.md                                    # 該對話全景說明與各輪次快速跳轉目錄
├── Turn-01-Agent-SDK-and-Ecosystem/             # 🗣️ 提問 + 📑 摘要 + 🏷️ 版本 + 🔄 Changelog
├── Turn-02-SDK-Use-Cases-and-Role-Division/
├── Turn-03-Agent-SDK-Code-Level-Implementation/
├── Turn-04-VS-Code-vs-Antigravity-2.0-Workflow/
├── Turn-05-Antigravity-IDE-vs-VS-Code-and-Engine/
├── Turn-06-to-07-AI-Agent-Ecosystem-Infographic/
├── Turn-08-to-09-Split-and-Fullscreen-4K-Infographics/
├── Turn-10-Global-Skill-2-Page-Infographic/
├── Turn-11-Tool-Comparison-4K-Infographics/
└── Turn-12-to-17-Dedicated-Repo-Governance/
```
