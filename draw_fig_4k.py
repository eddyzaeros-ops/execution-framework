"""
Draw fig.png (slide 37): 3840x2160 white minimalist English architecture figure
of the seven harness subsystems (D1-D7) + interface layer + session substrate.
All labels are taken from arXiv:2609.00006v1 (Sections 2.3, 6-13).
"""
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

matplotlib.rcParams['font.sans-serif'] = ['Segoe UI', 'Microsoft JhengHei', 'DejaVu Sans']

WHITE = '#FFFFFF'
INK = '#1F2933'
MUTED = '#5A6675'
LINE = '#CBD2D9'
SAGE = '#3B6E58'
TERRA = '#9E5A38'
SLATE = '#2C3E50'
OCHRE = '#B4782A'

fig = plt.figure(figsize=(12.8, 7.2), dpi=300)
fig.patch.set_facecolor(WHITE)
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, 128)
ax.set_ylim(0, 72)
ax.axis('off')


def box(x, y, w, h, edge, face=WHITE, lw=1.6, ls='-', r=1.2):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle=f"round,pad=0,rounding_size={r}",
                                linewidth=lw, edgecolor=edge, facecolor=face, linestyle=ls))


def subsystem(x, y, w, h, tag, title, items, color):
    box(x, y, w, h, color)
    box(x, y + h - 4.2, w, 4.2, color, face=color, r=1.2)
    ax.text(x + 1.2, y + h - 2.1, f"{tag}  {title}", fontsize=10.5, fontweight='bold', color=WHITE, va='center')
    for i, it in enumerate(items):
        ax.text(x + 1.4, y + h - 6.6 - i * 2.75, "•  " + it, fontsize=7.6, color=INK, va='center')


# Title
ax.text(64, 68.6, "Anatomy of a Coding-Agent Harness", fontsize=17, fontweight='bold', color=INK, ha='center', va='center')
ax.text(64, 65.4, "Agent = Model + Harness   ·   seven subsystems (D1–D7) + two cross-cutting surfaces   ·   arXiv:2609.00006v1",
        fontsize=8.5, color=MUTED, ha='center', va='center')

# Interface layer (left band)
box(3, 10, 13, 51, SLATE, face='#F4F6F8')
ax.text(9.5, 57.5, "INTERFACE\nLAYER", fontsize=9.5, fontweight='bold', color=SLATE, ha='center', va='center', linespacing=1.2)
for i, it in enumerate(["TUI", "CLI flags", "IDE protocol\n(ACP)", "HTTP server", "SDK"]):
    yy = 50 - i * 8.2
    box(4.5, yy - 3, 10, 6, LINE, r=0.8)
    ax.text(9.5, yy, it, fontsize=7.6, color=INK, ha='center', va='center')
ax.text(9.5, 12.2, "humans & programs\ndrive the harness", fontsize=6.6, color=MUTED, ha='center', va='center', style='italic')

# Column headers
cols = [(19, "RUNTIME CORE", SAGE), (55, "TOOLS & MEMORY", TERRA), (91, "GOVERNANCE & SCALE", OCHRE)]
for x, t, c in cols:
    ax.text(x + 17, 61.2, t, fontsize=10, fontweight='bold', color=c, ha='center', va='center')
    ax.plot([x, x + 34], [59.6, 59.6], color=c, lw=1.4)

# Column 1
subsystem(19, 35, 34, 23, "D1", "Agent Loop", [
    "Iterative ReAct loop (model → tools → observe)",
    "Reflection-augmented loop (Aider lint/test)",
    "Coordinator-worker pattern",
    "Stuck detection · step / cost limits",
    "Stop conditions (end_turn, no tool calls)"], SAGE)
subsystem(19, 10, 34, 23, "D2", "LLM Integration", [
    "Prompt assembly (static / dynamic sections)",
    "Prompt caching & cache boundaries",
    "Single-provider vs. multi-provider abstraction",
    "Extended thinking · reasoning effort",
    "Model routing"], SAGE)

# Column 2
subsystem(55, 35, 34, 23, "D3", "Tool & Action System", [
    "1 tool (bash) up to 109+ tools",
    "Exact string replacement · fuzzy cascades",
    "Deferred tool loading (tool search)",
    "Deterministic retrieval: ripgrep / glob",
    "tree-sitter symbols (Aider repo map)"], TERRA)
subsystem(55, 10, 34, 23, "D4", "Context & Memory", [
    "Linear history (Mini-SWE-Agent)",
    "Recursive summarization (Aider)",
    "Pluggable condensers (OpenHands)",
    "Threshold compaction (7/11 systems)",
    "Context files: AGENTS.md / CLAUDE.md"], TERRA)

# Column 3
subsystem(91, 43, 34, 15, "D5", "Safety & Permissions", [
    "Policy-as-code (Starlark) · lifecycle hooks",
    "LLM approval reviewer · human approval",
    "OS sandbox: Bubblewrap / Seatbelt"], OCHRE)
subsystem(91, 26.5, 34, 15, "D6", "Multi-Agent Orchestration", [
    "Sequential · parallel child sessions",
    "Thread tree (Codex) · recursive (Claude Code)",
    "Registry + protocol (ACP / A2A)"], OCHRE)
subsystem(91, 10, 34, 15, "D7", "Extensibility", [
    "SKILL.md skills (9/11) · MCP (8/11)",
    "Deferred skill loading (8 of 9)",
    "Lifecycle hooks · plugins · extensions"], OCHRE)

# Arrows: interface -> loop, loop <-> others
arr = dict(arrowstyle='-|>,head_width=0.25,head_length=0.45', lw=1.2, color=SLATE)
ax.annotate("", xy=(19, 46.5), xytext=(16, 46.5), arrowprops=arr)
ax.annotate("", xy=(36, 33.2), xytext=(36, 34.8), arrowprops=dict(arr, arrowstyle='<|-|>,head_width=0.25,head_length=0.45'))
ax.annotate("", xy=(55, 46.5), xytext=(53, 46.5), arrowprops=dict(arr, arrowstyle='<|-|>,head_width=0.25,head_length=0.45'))
ax.annotate("", xy=(55, 21.5), xytext=(53, 40), arrowprops=dict(arr, arrowstyle='<|-|>,head_width=0.25,head_length=0.45'))
ax.annotate("", xy=(89, 50), xytext=(91, 50), arrowprops=arr)
ax.annotate("", xy=(89, 40), xytext=(91, 34), arrowprops=arr)

# Session substrate (bottom band)
box(19, 2.2, 106, 5.6, SLATE, face='#F4F6F8', r=1.0)
ax.text(21, 5.0, "SESSION SUBSTRATE", fontsize=9, fontweight='bold', color=SLATE, va='center')
ax.text(46, 5.0, "transcripts  ·  persistence  ·  resume / fork   —   shared by several subsystems",
        fontsize=8, color=INK, va='center')
ax.text(3, 5.0, "0/11: agentic\nframeworks · code RAG", fontsize=6.4, color=TERRA, va='center', fontweight='bold')

fig.savefig('fig.png', dpi=300, facecolor=WHITE)
print("fig.png written")
