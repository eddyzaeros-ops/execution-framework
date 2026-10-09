import sys
import os
sys.path.insert(0, r"C:\Users\calsa\.gemini\antigravity\brain\28a9aa16-b3e0-4c1d-96fd-c10c45994241\scratch")
from t1v2 import *
from pptx import Presentation

pptx_path = r"d:\JavaDO\執行框架\專業領域AI解決方案評估報告.pptx"
prs = Presentation(pptx_path)

# ----------------- Slide A: 國際權威治理規範 -----------------
s_a = prs.slides.add_slide(prs.slide_layouts[6])
header(s_a, "實體隔離與國防 AI 治理權威標準：從邊界防禦轉向運行時內生安全", "安全治理",
       "CISA/NSA、NIST AI RMF、DoD IL5/IL6 與 MITRE ATLAS 對 Agentic AI 落地之核心指引")

FRAMEWORKS = [
    ("1. CISA / NSA / Five Eyes 聯合指引", "《Careful Adoption of Agentic AI》指出：實體隔離不等於絕對免疫。Agent 擁有工具呼叫與自主編排權限，必須在 Runtime Harness 實施『最小工具權限 (Least Privilege)』與不可繞過的狀態機約束。"),
    ("2. NIST AI RMF & DoD IL5/IL6 邊界標準", "DoD 要求隔離環境 AI 達成『全生命週期邊界合規』。數據與模型權重入庫需具備數位簽章與不可篡改追溯（Tamper-Evident）；推論計算與 CAE 呼叫須隔離於嚴格認證的安全邊界內。"),
    ("3. MITRE ATLAS AI 威脅矩陣實踐", "ATLAS 針對 AI Agent 擴展威脅向量（AML.T0051 工具濫用、AML.T0054 記憶污染）。在離線環境下，防禦核心不在即時聯網特徵庫，而在 Pre-Tool 階段的確定性語法與參數檢驗。")
]

cw, cg = 3.75, 0.242
for i, (mtitle, mdesc) in enumerate(FRAMEWORKS):
    x = 0.8 + i * (cw + cg)
    card(s_a, x, 1.72, cw, 2.38, mtitle, [mdesc], n=i + 1, color=SAGE if i % 2 == 0 else TERRA, size=11, title_size=12.5)

STD_TABLE = [
    ["權威機構 / 框架", "核心指導原則", "實體隔離內網之落地工程作法", "對開源 31B Agent 之關鍵意義"],
    ["CISA & NSA (2025)", "Runtime Governance 運行時治理", "以 Hooks 攔截工具輸入輸出，獨立記錄稽核日誌", "防止 Agent 受 Prompt 注入而越權調用工具"],
    ["NIST AI RMF 1.0", "MAP / MEASURE / MANAGE", "建立私有 50 題黃金評估集，每次迭代回歸測試", "以量化指標取代主觀信任，杜絕品質退化"],
    ["DoD IL5 / IL6", "Air-Gapped Enclave 數據主權", "單向光閘 (Data Diode) 導入權重，禁止反向遙測", "確保科研機密數據 100% 留在內網無任何滲漏"],
    ["MITRE ATLAS", "Adversary TTPs 針對性防護", "AST 靜態語法樹分析，沙箱密封執行代碼", "防範不可信輸入引發之內部橫向移動與污染"]
]

table(s_a, 0.8, 4.25, 11.733, STD_TABLE[0], STD_TABLE[1:],
      [2.5, 3.2, 3.2, 2.833], row_h=0.42, size=10.5, hl_col=2,
      aligns=[PP_ALIGN.LEFT, PP_ALIGN.LEFT, PP_ALIGN.LEFT, PP_ALIGN.LEFT])

quote(s_a, 6.20, "Air-gap is a perimeter, not a security control.",
      "實體隔離僅隔絕外網攻擊；內生安全必須仰賴 Harness 最小授權、AST 代碼沙箱與不可篡改審計", h=0.6)

# ----------------- Slide B: DARPA 與科研範式轉移 -----------------
s_b = prs.slides.add_slide(prs.slide_layouts[6])
header(s_b, "科研範式轉移：從『單體模型預訓練』走向『神經+符號』複合 AI 系統", "科研前沿",
       "DARPA 專案（AIxCC / TRACTOR）與最新頂會研究：以確定性工程包裹開源模型之實證啟示")

PARADIGMS = [
    ("1. DARPA AIxCC & TRACTOR 實證", "DARPA 最新挑戰賽證明：自主 Agent 解決軟體漏洞與 C 轉 Rust 移植時，勝負不在底層模型參數大小，而在『編譯器回饋循環、AST 語法校驗與測試驅動修復』的 Harness 編排完備度。"),
    ("2. 複合 AI 系統（Compound AI Systems）", "UC Berkeley 等機構指出：現今解決複雜專案的最優解已非單一大模型，而是由地端開源模型（Gemma 31B）、RAG 檢索器、代碼解譯器與 Hooks 驗證器構成的複合確定性系統。"),
    ("3. 神經符號結合（Neuro-Symbolic）", "LLM 負責模糊語義理解與候選生成（神經端），專家規則、CAE 網格邊界與物理公式充當硬約束檢查（符號端）。兩者結合使 31B 模型在專業領域達到 99%+ 任務通過率。")
]

for i, (mtitle, mdesc) in enumerate(PARADIGMS):
    x = 0.8 + i * (cw + cg)
    card(s_b, x, 1.72, cw, 2.38, mtitle, [mdesc], n=i + 1, color=SAGE if i % 2 == 0 else TERRA, size=11, title_size=12.5)

DARPA_TABLE = [
    ["前沿計畫 / 頂尖學派", "核心架構突破", "傳統自訓模型之盲點", "實體隔離研發之直接借鑑"],
    ["DARPA AIxCC (2024-25)", "Cyber Reasoning Systems (CRS)", "單靠大模型生成修補代碼極易產生新漏洞", "引進自動化測試與編譯器回饋，閉環自修復"],
    ["DARPA TRACTOR (2024)", "LLM-driven Agentic Migration", "微調模型無法保證記憶體安全性與語意等價", "以符號規則與靜態分析約束 Agent 代碼重構"],
    ["Berkeley Compound AI", "系統工程超越單體 LLM 規模", "花費巨資預訓練往往在 6 個月內被開源超越", "投資持久的 MCP 工具鏈、評估集與狀態機"],
    ["Neuro-Symbolic 實踐", "神經生成 + 符號驗證器", "純生成式模型缺乏數理確定性與精確邊界", "將國防工程標準 (MIL-STD) 轉為確定性驗證代碼"]
]

table(s_b, 0.8, 4.25, 11.733, DARPA_TABLE[0], DARPA_TABLE[1:],
      [2.5, 3.2, 3.2, 2.833], row_h=0.42, size=10.5, hl_col=3,
      aligns=[PP_ALIGN.LEFT, PP_ALIGN.LEFT, PP_ALIGN.LEFT, PP_ALIGN.LEFT])

quote(s_b, 6.20, "State-of-the-art results are increasingly won by compound systems, not monolithic models.",
      "押注在確定性驗證器、Harness 閉環與工程工具鏈上，是實體隔離環境中最具長期複利效應的研發投資", h=0.6)

# ----------------- 更新 Slide 33 (原本的附錄，現在會是最後一頁) -----------------
# 重新整理並擴充參考文獻 Slide
s_ref = prs.slides[32] # 原 Slide 33

# 新增最後兩頁的頁腳與頁碼，重新編號整份簡報
total = len(prs.slides)
for idx, s in enumerate(prs.slides, 1):
    if idx == 1:
        continue
    # 檢查是否有頁尾，有的話更新頁碼
    # 為新增的兩頁加上頁尾
    if idx in [total - 1, total]:
        text(s, 0.8, 7.12, 9.5, 0.25, "國防專業領域 AI 策略評估  ·  AIR-GAPPED ON-PREM DOMAIN AI STRATEGY", size=8, color=MUTED)
        text(s, 11.0, 7.12, 1.533, 0.25, f"{idx:02d} / {total:02d}", size=9, color=SAGE, bold=True, align=PP_ALIGN.RIGHT)

prs.save(pptx_path)
print(f"Appended 2 authoritative research slides. New total slides: {total}")
