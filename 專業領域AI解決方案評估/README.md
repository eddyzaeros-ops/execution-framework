# 專案系列對話：專業領域AI解決方案評估

本資料夾彙整此專案對話系列中所有協同研析、架構設計、投影片產出、4K 雙頁資訊圖表與 Obsidian 知識庫之完整歷程、使用者原始提問、各輪次文件摘要、版本收斂歷程與實體資產。

---

## 🧭 對話輪次導航矩陣 (Turn Navigation Matrix)

| 輪次代號 | 研析與模組主題 | 版本 | 核心產出物 / 資產清單 | 模組直達連結 |
| :--- | :--- | :---: | :--- | :--- |
| **Turn 01** | 專業領域 AI 解決方案四種技術路線評估 | `v1.0.0` | `docs/專業領域AI解決方案評估報告.md` | [Turn-01 README](file:///./Turn-01-專業領域四種路線評估報告/README.md) |
| **Turn 02** | 國防研發機敏限制、F2T2 無人機殺傷鏈與地端選型 | `v1.1.0` | `docs/國防研發AI方案評估報告_地端版.md` | [Turn-02 README](file:///./Turn-02-國防地端環境限制與落地戰略/README.md) |
| **Turn 03** | 專家權威背書、Harness 生態系與差距雷達圖 | `v1.2.0` | `assets/radar_chart.png`, `curve_chart.png`, `expert_consensus_chart.png`, `code/` | [Turn-03 README](file:///./Turn-03-權威專家觀點與Harness生態系調研/README.md) |
| **Turn 04** | 單卡 Gemma-3-27B 高承載與 5W1H Sub-Agent 編排 | `v1.3.0` | `code/part_gemma_p3.py`, `extra_d.py` | [Turn-04 README](file:///./Turn-04-實戰架構深化_Gemma31B與Sub-Agent/README.md) |
| **Turn 05** | Context Engineering、Git 原生審計與第二大腦知識沉澱 | `v1.4.0` | `code/part_memory_graph.py` | [Turn-05 README](file:///./Turn-05-第二大腦級記憶架構_Git與Obsidian/README.md) |
| **Turn 06** | 純白極簡 4K 雙頁式視覺系統 (fig.png + doc.png) | `v1.5.0` | `assets/fig.png`, `assets/doc.png`, `code/build_2page_infographic.py` | [Turn-06 README](file:///./Turn-06-實體隔離運作全景4K雙頁資訊圖表/README.md) |
| **Turn 07** | 國際權威資安標準綜整、OWASP AISVS 1.0 評測與 37 頁定稿簡報 | `v1.6.0` | `pptx/專業領域AI解決方案評估報告.pptx` (37 頁), `code/` | [Turn-07 README](file:///./Turn-07-國際權威標準_CISA_DARPA與AISVS評測/README.md) |
| **Turn 08** | Obsidian 結構化知識庫沉澱、Mermaid 響應式優化與全域治理 | `v2.0.0` | `docs/` (00 至 06 篇完整 Obsidian 雙向鏈結筆記) | [Turn-08 README](file:///./Turn-08-Obsidian思維知識庫沉澱與圖表優化/README.md) |

---

## 🏛️ 模組化目錄結構

```text
專業領域AI解決方案評估/
├── README.md                                                     # 對話系列總體導航與主題導航矩陣
├── Turn-01-專業領域四種路線評估報告/                             # 🗣️ 提問 + 📑 摘要 + 🏷️ 版本 + 🔄 Changelog
│   └── docs/ (專業領域AI解決方案評估報告.md)
├── Turn-02-國防地端環境限制與落地戰略/
│   └── docs/ (國防研發AI方案評估報告_地端版.md)
├── Turn-03-權威專家觀點與Harness生態系調研/
│   ├── assets/ (radar_chart.png, expert_consensus_chart.png, curve_chart.png)
│   └── code/ (part_radar.py, part_gap_detail.py, add_literature_slides.py)
├── Turn-04-實戰架構深化_Gemma31B與Sub-Agent/
│   └── code/ (part_gemma_p3.py, extra_d.py, check_s33.py)
├── Turn-05-第二大腦級記憶架構_Git與Obsidian/
│   └── code/ (part_memory_graph.py)
├── Turn-06-實體隔離運作全景4K雙頁資訊圖表/
│   ├── assets/ (fig.png, doc.png)
│   └── code/ (build_2page_infographic.py, update_doc_large_font.py)
├── Turn-07-國際權威標準_CISA_DARPA與AISVS評測/
│   ├── pptx/ (專業領域AI解決方案評估報告.pptx - 37 頁定稿)
│   └── code/ (add_aisvs_slides.py, populate_aisvs_slides.py, export_aisvs_png.py)
└── Turn-08-Obsidian思維知識庫沉澱與圖表優化/
    └── docs/ (00_總體架構與導讀.md ~ 06_OWASP_AISVS_1.0_評測矩陣.md)
```

---

## 🛡️ 專案治理原則落實

1. **Clean Root Policy**：專案根目錄保持純淨，絕無對話生成的離散文件。
2. **Turn-Specific Subdirectories**：每輪對話成果均收納至對應輪次之子目錄 (`docs/`, `pptx/`, `code/`, `html/`, `assets/`)。
3. **Verbatim User Requests**：每輪 `README.md` 開頭均完整留存該輪次所有使用者原始提問，做到 100% 審計可追溯。
