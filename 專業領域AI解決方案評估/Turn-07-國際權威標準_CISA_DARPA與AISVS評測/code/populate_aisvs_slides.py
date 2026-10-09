import sys
import os
sys.path.insert(0, r"C:\Users\calsa\.gemini\antigravity\brain\28a9aa16-b3e0-4c1d-96fd-c10c45994241\scratch")
from t1v2 import *
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor

pptx_path = r"d:\JavaDO\執行框架\專業領域AI解決方案評估報告.pptx"
prs = Presentation(pptx_path)

# =========================================================================
# 投影片 1 (Slide 35, 索引 34): OWASP AISVS 1.0 標準體系與實體隔離三大「落地工程卡點」
# =========================================================================
s35 = prs.slides[34]
header(s35, "OWASP AISVS 1.0 標準體系：Chapter 9 & 10 與三大落地工程卡點", "安全驗證標準",
       "全球首部 AI 系統技術級驗證標準（2026 正式版）：將 Agent 編排、MCP 整合轉化為確定性工程防線")

AISVS_PILLARS = [
    ("1. 全球首部 AI 技術級驗證標準", "AISVS 1.0 承襲 ASVS 嚴謹架構，專門收錄 191 條針對 AI 攻擊面的檢驗規範。在 12 大章節中，最關鍵核心在於 Chapter 9（Agent 編排安全）與 Chapter 10（MCP 協定整合安全）。"),
    ("2. 突破 Air-Gap Fallacy 迷思", "CISA 與 OWASP 共同強調：實體隔離僅隔絕外網，隔離內的 Agent 仍具備工具調用與自主執行權限。若缺乏運行時（Runtime）檢驗，不可信內容仍可造成內部提權與資料污染。"),
    ("3. 驗證導向的工程驗收閉環", "AISVS 的每一條規範均以『Verify that...』客觀可測試條款呈現。研發團隊可直接將其轉化為 CI/CD 流程中的自動化安全評估測試案例，杜絕品質退化。")
]

cw, cg = 3.75, 0.242
for i, (mtitle, mdesc) in enumerate(AISVS_PILLARS):
    x = 0.8 + i * (cw + cg)
    card(s35, x, 1.70, cw, 2.30, mtitle, [mdesc], n=i + 1, color=SAGE if i % 2 == 0 else TERRA, size=10.5, title_size=12)

GATE_TABLE = [
    ["實體隔離三大落地工程卡點", "對應 AISVS 1.0 核心條款", "傳統作法之風險與破綻", "Harness 確定性工程解法 (Gemma 31B)"],
    ["卡點 1：Pre-Tool 靜態審查與 AST 阻斷", "C9.3 工具授權 / C10.1 MCP 檢驗", "任由模型生成腳本直通系統，易致越權", "代碼執行前由 Pre-Tool Hook 解析 AST 樹，攔截危險呼叫"],
    ["卡點 2：Human-in-the-Loop 簽核閥門", "C9.2 高衝擊動作強制人工審批", "缺乏審批機制，不可逆操作（覆寫庫）自動生效", "依 Action Risk Matrix 標記紅線動作，強制掛起線程待簽核"],
    ["卡點 3：密封沙箱與不可篡改審計", "C9.1 預算熔斷 / C12.1 唯讀審計", "無隔離環境易導致逃逸，日誌可被竄改", "斷網 Docker/gVisor 密封運行，UUID Trace 寫入唯讀稽核儲存"]
]

table(s35, 0.8, 4.12, 11.733, GATE_TABLE[0], GATE_TABLE[1:],
      [2.7, 2.5, 3.2, 3.333], row_h=0.40, size=9.8, hl_col=3,
      aligns=[PP_ALIGN.LEFT, PP_ALIGN.LEFT, PP_ALIGN.LEFT, PP_ALIGN.LEFT])

quote(s35, 6.30, "AISVS 1.0 turns probabilistic AI into verifiable, deterministic engineering.",
      "以 Chapter 9 & 10 為藍本，將實體隔離的三大工程卡點固化為不可繞過的 Harness 護欄", h=0.6)

# =========================================================================
# 投影片 2 (Slide 36, 索引 35): OWASP AISVS 1.0 AI Agent 核心評測矩陣
# =========================================================================
s36 = prs.slides[35]
header(s36, "OWASP AISVS 1.0 AI Agent 核心評測矩陣：實體隔離落地驗收標準", "評測標準矩陣",
       "依據 AISVS Chapter 9 & 10 提煉之 7 大核心驗證維度、工程實作做法與自動化 Evals 測試案例")

MATRIX_DATA = [
    ["評測驗證維度", "AISVS 1.0 條款核心要求", "實體隔離工程實作做法 (Harness)", "自動化 Evals 測試案例 (50 題黃金集)"],
    ["1. 執行預算與熔斷機制", "C9.1 驗證具備執行步數、Token 與死循環熔斷", "狀態機計數器（步數 <= 8, Token <= 32K）", "注入歧義悖論指令，驗證是否強制中斷而非無限遞迴"],
    ["2. 關鍵動作人機簽核閘門", "C9.2 驗證不可逆與高衝擊操作強制掛起", "Action Risk Matrix 標記，強制暫停發出請求", "誘導 Agent 嘗試刪庫或覆蓋代碼，驗證是否 100% 觸發簽核"],
    ["3. 工具隔離與最小權限", "C9.3 驗證無隱式權限，工具採最小 RBAC 授權", "Docker/gVisor 密封沙箱，禁開網路 Namespace", "以生成腳本測試逃逸與敏感路徑讀取，驗證是否遭沙箱阻絕"],
    ["4. 代理身分與動態憑證", "C9.4 驗證呼叫微服務使用短效動態憑證", "內網 IAM 簽發短效 JWT（TTL < 15 分鐘）", "截取過期 Token 或偽造身份，驗證 MCP 服務是否立即拒絕"],
    ["5. 記憶庫防護與反污染", "C8/C9 驗證長期記憶具備寫入關卡防污染", "候選記憶經專家 PR 審核後才合併至 Git", "注入具備誤導參數的錯誤經驗，驗證是否被阻擋於暫存區"],
    ["6. MCP 協定與間接注入", "C10.1 驗證 MCP Schema 型別校驗與輸出消殺", "Pydantic 強制校驗，AST 剥離隱藏 Prompt 指令", "在文件摻入『忽略前述指令』之 Payload，驗證是否被消殺"],
    ["7. 不可篡改稽核軌跡", "C12.1 驗證全推論鏈與工具日誌寫入唯讀儲存", "每步附唯一 UUID Trace ID，Append-only 落盤", "審查日誌連續性與校驗碼，確認無未記錄之工具調用或後門"]
]

table(s36, 0.8, 1.70, 11.733, MATRIX_DATA[0], MATRIX_DATA[1:],
      [2.3, 2.8, 3.3, 3.333], row_h=0.55, size=9.8, hl_col=3,
      aligns=[PP_ALIGN.LEFT, PP_ALIGN.LEFT, PP_ALIGN.LEFT, PP_ALIGN.LEFT])

quote(s36, 6.25, "Verify every step. Trust no implicit output.",
      "以 AISVS 1.0 的 7 大維度建立常態化紅藍對抗評測集，為國防開源 31B 模型提供軍規可靠度保證", h=0.6)

# =========================================================================
# 投影片 3 (Slide 37, 索引 36): 更新原附錄表格，加入 OWASP AISVS 1.0 出處
# =========================================================================
s37 = prs.slides[36]
for sh in s37.shapes:
    if sh.has_table:
        sp = sh._element
        sp.getparent().remove(sp)
        break

NEW_REFS_ALL = [
    ["OWASP (2026)", "AISVS 1.0: AI Security Verification Standard (Chapter 9 & 10 核心規範)", "owasp.org/www-project-ai-security-verification-standard"],
    ["CISA & NSA (2025)", "Careful Adoption of Agentic AI Services (Five Eyes 聯合運行時治理指引)", "cisa.gov / nsa.gov"],
    ["NIST (2024)", "Artificial Intelligence Risk Management Framework (AI RMF 1.0) & CSF 2.0", "nist.gov/itl/ai-risk-management-framework"],
    ["MITRE (2024-25)", "ATLAS: Adversarial Threat Landscape for AI Systems (Agent 威脅矩陣)", "atlas.mitre.org"],
    ["DoD CIO (2024)", "DoD Cloud and On-Prem AI Security Standards (Impact Level IL5/IL6 規範)", "dodcio.defense.gov"],
    ["DARPA (2024-25)", "AI Cyber Challenge (AIxCC) & TRACTOR Program (自主 Agent 代碼遷移)", "darpa.mil/program/ai-cyber-challenge"],
    ["Zaharia et al. (2024)", "The Shift from Models to Compound AI Systems (UC Berkeley BAIR 實證)", "bair.berkeley.edu/blog/2024/02/18/compound-ai-systems"],
    ["Anthropic (2024-25)", "Building effective agents & Effective context engineering (Rot 實證)", "anthropic.com/engineering"],
    ["R. Sutton (2019)", "The Bitter Lesson (通用架構與算力超越手工特化權重)", "incompleteideas.net/IncIdeas/BitterLesson.html"],
    ["S. Willison (2025)", "The lethal trifecta for AI agents (Agent 安全外洩三要素分析)", "simonwillison.net"]
]

headers = ["權威作者 / 官方機構", "標題與核心主旨", "來源網址 / 出處"]
table(s37, 0.8, 1.85, 11.733, headers, NEW_REFS_ALL,
      [2.6, 5.7, 3.433], row_h=0.45, size=9.5,
      aligns=[PP_ALIGN.LEFT, PP_ALIGN.LEFT, PP_ALIGN.LEFT])

# 校正所有 37 頁的頁碼
total = len(prs.slides)
for idx, s in enumerate(prs.slides, 1):
    if idx == 1:
        continue
    found_page = False
    for sh in s.shapes:
        if sh.has_text_frame and "/" in sh.text_frame.text and len(sh.text_frame.text.strip()) <= 10:
            sh.text_frame.text = f"{idx:02d} / {total:02d}"
            p = sh.text_frame.paragraphs[0]
            p.alignment = PP_ALIGN.RIGHT
            p.font.name = FONT
            p.font.size = Pt(9)
            p.font.color.rgb = SAGE
            p.font.bold = True
            found_page = True
            break
    if not found_page:
        box_f = s.shapes.add_textbox(Inches(0.8), Inches(7.12), Inches(9.5), Inches(0.25))
        tf_f = box_f.text_frame; tf_f.word_wrap = True
        p_f = tf_f.paragraphs[0]; p_f.text = "國防專業領域 AI 策略評估  ·  AIR-GAPPED ON-PREM DOMAIN AI STRATEGY"
        p_f.font.name = FONT; p_f.font.size = Pt(8); p_f.font.color.rgb = RGBColor(0x6C, 0x7A, 0x89)

        box_p = s.shapes.add_textbox(Inches(11.0), Inches(7.12), Inches(1.533), Inches(0.25))
        tf_p = box_p.text_frame; tf_p.word_wrap = True
        p_p = tf_p.paragraphs[0]; p_p.text = f"{idx:02d} / {total:02d}"
        p_p.alignment = PP_ALIGN.RIGHT
        p_p.font.name = FONT; p_p.font.size = Pt(9); p_p.font.color.rgb = SAGE; p_p.font.bold = True

prs.save(pptx_path)
print(f"Successfully populated slides 35, 36, 37 with clean layout. Total slides: {total}")
