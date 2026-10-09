"""
Matplotlib Redraw Script for arXiv:2609.00006v1 Figures 1, 2, and 6.
ENLARGED TYPOGRAPHY & ENHANCED VISUAL CONTRAST.
Strictly adopts Template 1 color palette:
- Canvas: #F5F2EB
- Card: #FDFCFA
- Borders: #D6CEBF, #B5AA98
- Brand Sage: #3B6E58
- Brand Terra: #9E5A38
- Brand Slate: #2C3E50
- Brand Ochre: #B4782A
- Text Charcoal: #232D38
- Font: Microsoft JhengHei / Segoe UI
"""

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

matplotlib.rcParams['font.sans-serif'] = ['Microsoft JhengHei', 'Segoe UI', 'DejaVu Sans']
matplotlib.rcParams['axes.unicode_minus'] = False

C_CANVAS = '#F5F2EB'
C_CARD = '#FDFCFA'
C_BORDER = '#D6CEBF'
C_BORDER_DARK = '#B5AA98'
C_SAGE = '#3B6E58'
C_TERRA = '#9E5A38'
C_SLATE = '#2C3E50'
C_OCHRE = '#B4782A'
C_TEXT_DARK = '#232D38'
C_TEXT_MUTED = '#5A6675'

# ------------------------------------------------------------------------------
# FIGURE 1: Canonical Anatomy of a Coding-Agent Harness (Enlarged Fonts)
# ------------------------------------------------------------------------------
def draw_figure_1():
    fig, ax = plt.subplots(figsize=(14, 6.8), dpi=300)
    fig.patch.set_facecolor(C_CANVAS)
    ax.set_facecolor(C_CANVAS)
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 6.8)
    ax.axis('off')

    # Outer Harness Boundary
    harness_rect = FancyBboxPatch(
        (0.5, 0.4), 13.0, 5.9,
        boxstyle="round,pad=0.1,rounding_size=0.35",
        linewidth=2.2, edgecolor=C_BORDER_DARK, facecolor=C_CARD, linestyle='--'
    )
    ax.add_patch(harness_rect)
    ax.text(0.85, 5.95, "[Runtime Boundary] Coding-Agent Harness: Seven Subsystems + Two Cross-Cutting Surfaces", 
            fontsize=13.5, fontweight='bold', color=C_SAGE)

    def draw_node(x, y, w, h, title, subtitle, bg_color, border_color, title_color=C_TEXT_DARK, bold_tag=None):
        patch = FancyBboxPatch(
            (x, y), w, h,
            boxstyle="round,pad=0.08,rounding_size=0.2",
            linewidth=1.6, edgecolor=border_color, facecolor=bg_color
        )
        ax.add_patch(patch)
        if bold_tag:
            ax.text(x + w/2, y + h - 0.32, bold_tag, fontsize=11.5, fontweight='bold', color=C_TERRA, ha='center', va='center')
        ax.text(x + w/2, y + h*0.56 if subtitle else y + h*0.5, title, fontsize=13.0, fontweight='bold', color=title_color, ha='center', va='center')
        if subtitle:
            ax.text(x + w/2, y + 0.32, subtitle, fontsize=10.5, fontweight='bold', color=C_TEXT_MUTED, ha='center', va='center')

    # Interface Layer (Left)
    draw_node(0.9, 2.5, 2.6, 1.5, "Interface Layer", "TUI / CLI / IDE / HTTP / SDK", '#EBF0F5', C_SLATE, title_color=C_SLATE, bold_tag="[INTERFACE]")

    # Orchestration (Bottom Left)
    draw_node(0.9, 0.7, 2.6, 1.4, "Orchestration", "sub-agents / protocols", '#F9F5EC', C_OCHRE, title_color=C_OCHRE, bold_tag="D6")

    # Central Column: D2 LLM Integration (Top), D1 Agent Loop (Center), D4 Memory (Bottom)
    draw_node(4.2, 4.35, 2.8, 1.5, "LLM Integration", "Prompt assembly / Caching", '#FBEFEA', C_TERRA, title_color=C_TERRA, bold_tag="D2")
    draw_node(4.2, 2.5, 2.8, 1.5, "Agent Loop", "Control Flow / Stop / Stuck", '#EBF2EE', C_SAGE, title_color=C_SAGE, bold_tag="D1 (HEART)")
    draw_node(4.2, 0.7, 2.8, 1.4, "Memory & Context", "Compaction / Summarization", '#EBF2EE', C_SAGE, title_color=C_SAGE, bold_tag="D4")

    # Right Column: D5 Safety (Top), D3 Tools (Center), D7 Extensibility (Bottom)
    draw_node(7.8, 4.35, 2.8, 1.5, "Safety & Permissions", "Starlark / Sandboxes / HITL", '#FBEFEA', C_TERRA, title_color=C_TERRA, bold_tag="D5")
    draw_node(7.8, 2.5, 2.8, 1.5, "Tool & Action System", "Edit / Shell / Search", '#EBF2EE', C_SAGE, title_color=C_SAGE, bold_tag="D3")
    draw_node(11.0, 2.5, 2.2, 1.5, "Session Substrate", "transcripts / resume / fork", '#EBF0F5', C_SLATE, title_color=C_SLATE, bold_tag="[SHARED]")
    draw_node(7.8, 0.7, 5.3, 1.4, "Extensibility Standards", "SKILL.md (9/11) · MCP (8/11) · Lifecycle Hooks", '#F2EFE9', C_SLATE, title_color=C_SLATE, bold_tag="D7")

    # Flow arrows
    arrow_kw = dict(arrowstyle='<|-|>,head_width=0.35,head_length=0.45', lw=1.8, color=C_SLATE)
    arrow_fwd = dict(arrowstyle='-|>,head_width=0.35,head_length=0.45', lw=1.8, color=C_SLATE)
    
    # Interface <-> Agent Loop
    ax.annotate("", xy=(4.2, 3.25), xytext=(3.5, 3.25), arrowprops=arrow_kw)
    # Agent Loop <-> LLM Integration
    ax.annotate("", xy=(5.6, 4.35), xytext=(5.6, 4.0), arrowprops=arrow_kw)
    # Agent Loop <-> Memory
    ax.annotate("", xy=(5.6, 2.1), xytext=(5.6, 2.5), arrowprops=arrow_kw)
    # Agent Loop <-> Tools
    ax.annotate("", xy=(7.8, 3.25), xytext=(7.0, 3.25), arrowprops=arrow_kw)
    # Safety -> Tools
    ax.annotate("", xy=(9.2, 4.0), xytext=(9.2, 4.35), arrowprops=arrow_fwd)
    # Extensibility -> Tools
    ax.annotate("", xy=(9.2, 2.5), xytext=(9.2, 2.1), arrowprops=arrow_fwd)
    ax.annotate("", xy=(11.0, 3.25), xytext=(10.6, 3.25), arrowprops=dict(arrowstyle='<|-|>,head_width=0.3,head_length=0.4', lw=1.6, color=C_SLATE, ls='--'))
    # Orchestration -> Agent Loop (dashed feed)
    ax.annotate("", xy=(4.2, 1.4), xytext=(3.5, 1.4), arrowprops=dict(arrowstyle='<|-|>,head_width=0.3,head_length=0.4', lw=1.6, color=C_OCHRE, ls='--'))

    plt.tight_layout()
    plt.savefig('fig1_matplotlib.png', dpi=300, facecolor=C_CANVAS)
    plt.close()
    print("Successfully generated fig1_matplotlib.png with enlarged text")

# ------------------------------------------------------------------------------
# FIGURE 2: Three Agent Loop Paradigms (Enlarged Fonts)
# ------------------------------------------------------------------------------
def draw_figure_2():
    fig, axes = plt.subplots(1, 3, figsize=(14, 6.2), dpi=300)
    fig.patch.set_facecolor(C_CANVAS)

    titles = ["(a) Iterative Loop (OpenHands/Codex)", "(b) Reflection-Augmented (Aider)", "(c) Coordinator-Worker (Claude/Codex)"]
    sub_headers = ["Action-Observation Cycle", "Linter & AST Self-Correction", "Sub-agent Hierarchical Dispatch"]

    for i, ax in enumerate(axes):
        ax.set_facecolor(C_CARD)
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.axis('off')
        
        rect = FancyBboxPatch((0.2, 0.2), 9.6, 9.6, boxstyle="round,pad=0.1,rounding_size=0.25", linewidth=1.5, edgecolor=C_BORDER, facecolor=C_CARD)
        ax.add_patch(rect)
        ax.text(5.0, 9.25, titles[i], fontsize=12.0, fontweight='bold', color=C_SLATE, ha='center')
        ax.text(5.0, 8.65, sub_headers[i], fontsize=10.5, fontweight='bold', color=C_TEXT_MUTED, ha='center')

    arr = dict(arrowstyle='-|>,head_width=0.28,head_length=0.38', lw=1.6, color=C_SLATE)

    # Panel A: Iterative
    ax_a = axes[0]
    nodes_a = [
        (2.5, 6.9, 5.0, 1.05, "Prompt Assembly", '#EBF0F5', C_SLATE),
        (2.5, 5.1, 5.0, 1.05, "LLM Inference", '#FBEFEA', C_TERRA),
        (2.5, 3.3, 5.0, 1.05, "Tool Execution", '#EBF2EE', C_SAGE),
        (2.5, 1.5, 5.0, 1.05, "Observe Output", '#F9F5EC', C_OCHRE),
    ]
    for x, y, w, h, t, bg, bc in nodes_a:
        p = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.05,rounding_size=0.15", linewidth=1.4, edgecolor=bc, facecolor=bg)
        ax_a.add_patch(p)
        ax_a.text(x + w/2, y + h/2, t, fontsize=12.0, fontweight='bold', color=C_TEXT_DARK, ha='center', va='center')

    ax_a.annotate("", xy=(5.0, 6.15), xytext=(5.0, 6.9), arrowprops=arr)
    ax_a.annotate("", xy=(5.0, 4.35), xytext=(5.0, 5.1), arrowprops=arr)
    ax_a.annotate("", xy=(5.0, 2.55), xytext=(5.0, 3.3), arrowprops=arr)
    # Loop back
    ax_a.annotate("", xy=(7.5, 7.4), xytext=(7.5, 2.05), arrowprops=dict(arrowstyle='-|>,head_width=0.28,head_length=0.38', lw=1.6, color=C_SAGE, connectionstyle="arc3,rad=-0.55"))
    ax_a.text(9.0, 4.7, "Next Turn\n(Repeat)", fontsize=10.5, fontweight='bold', color=C_SAGE, ha='center')

    # Panel B: Reflection
    ax_b = axes[1]
    nodes_b = [
        (2.5, 7.1, 5.0, 0.95, "Prompt Assembly", '#EBF0F5', C_SLATE),
        (2.5, 5.5, 5.0, 0.95, "LLM Inference", '#FBEFEA', C_TERRA),
        (2.5, 3.9, 5.0, 0.95, "Apply Diff Patch", '#EBF2EE', C_SAGE),
        (2.5, 2.3, 5.0, 0.95, "Linter / AST Tests", '#FDEFEF', C_TERRA),
        (2.5, 0.7, 5.0, 0.95, "Pass Verification?", '#F9F5EC', C_OCHRE),
    ]
    for x, y, w, h, t, bg, bc in nodes_b:
        p = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.05,rounding_size=0.15", linewidth=1.4, edgecolor=bc, facecolor=bg)
        ax_b.add_patch(p)
        ax_b.text(x + w/2, y + h/2, t, fontsize=11.5, fontweight='bold', color=C_TEXT_DARK, ha='center', va='center')

    ax_b.annotate("", xy=(5.0, 6.45), xytext=(5.0, 7.1), arrowprops=arr)
    ax_b.annotate("", xy=(5.0, 4.85), xytext=(5.0, 5.5), arrowprops=arr)
    ax_b.annotate("", xy=(5.0, 3.25), xytext=(5.0, 3.9), arrowprops=arr)
    ax_b.annotate("", xy=(5.0, 1.65), xytext=(5.0, 2.3), arrowprops=arr)
    # Error Reflection Loop
    ax_b.annotate("", xy=(2.5, 7.55), xytext=(2.5, 1.15), arrowprops=dict(arrowstyle='-|>,head_width=0.28,head_length=0.38', lw=1.6, color=C_TERRA, connectionstyle="arc3,rad=-0.52"))
    ax_b.text(1.2, 4.4, "Errors\n(Reflect <= 3x)", fontsize=10.0, fontweight='bold', color=C_TERRA, ha='center')
    # Success exit
    ax_b.annotate("", xy=(8.7, 1.15), xytext=(7.5, 1.15), arrowprops=arr)
    ax_b.text(8.9, 1.65, "Done", fontsize=11.0, fontweight='bold', color=C_SAGE, ha='center')

    # Panel C: Coordinator-Worker
    ax_c = axes[2]
    p_coord = FancyBboxPatch((2.5, 6.9), 5.0, 1.1, boxstyle="round,pad=0.05,rounding_size=0.15", linewidth=1.6, edgecolor=C_TERRA, facecolor='#FBEFEA')
    ax_c.add_patch(p_coord)
    ax_c.text(5.0, 7.45, "Coordinator Lead", fontsize=12.5, fontweight='bold', color=C_TERRA, ha='center', va='center')

    workers = [
        (0.6, 4.1, 2.6, 1.25, "Worker 1\n(Research)", '#EBF0F5', C_SLATE),
        (3.7, 4.1, 2.6, 1.25, "Worker 2\n(Implement)", '#EBF2EE', C_SAGE),
        (6.8, 4.1, 2.6, 1.25, "Worker 3\n(Verify)", '#F9F5EC', C_OCHRE),
    ]
    for x, y, w, h, t, bg, bc in workers:
        p = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.05,rounding_size=0.15", linewidth=1.4, edgecolor=bc, facecolor=bg)
        ax_c.add_patch(p)
        ax_c.text(x + w/2, y + h/2, t, fontsize=10.8, fontweight='bold', color=C_TEXT_DARK, ha='center', va='center')

    p_syn = FancyBboxPatch((2.5, 1.5), 5.0, 1.1, boxstyle="round,pad=0.05,rounding_size=0.15", linewidth=1.5, edgecolor=C_SAGE, facecolor='#EBF2EE')
    ax_c.add_patch(p_syn)
    ax_c.text(5.0, 2.05, "Synthesize Results", fontsize=12.0, fontweight='bold', color=C_SAGE, ha='center', va='center')

    # Dispatch & Synthesize arrows
    ax_c.annotate("", xy=(1.9, 5.35), xytext=(3.8, 6.9), arrowprops=arr)
    ax_c.annotate("", xy=(5.0, 5.35), xytext=(5.0, 6.9), arrowprops=arr)
    ax_c.annotate("", xy=(8.1, 5.35), xytext=(6.2, 6.9), arrowprops=arr)

    ax_c.annotate("", xy=(3.8, 2.6), xytext=(1.9, 4.1), arrowprops=arr)
    ax_c.annotate("", xy=(5.0, 2.6), xytext=(5.0, 4.1), arrowprops=arr)
    ax_c.annotate("", xy=(6.2, 2.6), xytext=(8.1, 4.1), arrowprops=arr)

    plt.tight_layout()
    plt.savefig('fig2_matplotlib.png', dpi=300, facecolor=C_CANVAS)
    plt.close()
    print("Successfully generated fig2_matplotlib.png with enlarged text")

# ------------------------------------------------------------------------------
# FIGURE 6: Six Multi-Agent Orchestration Patterns (Enlarged Fonts)
# ------------------------------------------------------------------------------
def draw_figure_6():
    fig, axes = plt.subplots(2, 3, figsize=(14, 8.2), dpi=300)
    fig.patch.set_facecolor(C_CANVAS)

    topo_info = [
        ("(1) Single-agent", "Mini-SWE-Agent, Aider, Pi core", "No spawn tool; single ReAct loop"),
        ("(2) Sequential delegation", "Mistral Vibe", "Parent blocks; one child at a time"),
        ("(3) Parallel child sessions", "OpenHands, OpenCode", "Concurrent; separate histories"),
        ("(4) Hierarchical thread tree", "Codex CLI", "Depth-tracked tree; CSV fan-out"),
        ("(5) Recursive composition", "Claude Code", "Any agent spawns agents; shared cache"),
        ("(6) Registry + protocol", "Gemini CLI, OpenClaw, Hermes", "Process boundary; ACP / A2A")
    ]

    arr = dict(arrowstyle='-|>,head_width=0.28,head_length=0.38', lw=1.5, color=C_SLATE)
    arr_dashed = dict(arrowstyle='-|>,head_width=0.28,head_length=0.38', lw=1.5, color=C_SLATE, ls='--')

    for idx, (title, systems, note) in enumerate(topo_info):
        r, c = idx // 3, idx % 3
        ax = axes[r, c]
        ax.set_facecolor(C_CARD)
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.axis('off')

        rect = FancyBboxPatch((0.2, 0.2), 9.6, 9.6, boxstyle="round,pad=0.1,rounding_size=0.22", linewidth=1.4, edgecolor=C_BORDER, facecolor=C_CARD)
        ax.add_patch(rect)
        ax.text(5.0, 9.25, title, fontsize=12.0, fontweight='bold', color=C_SLATE, ha='center')
        ax.text(5.0, 8.55, systems, fontsize=10.0, fontweight='bold', color=C_TERRA, ha='center')
        ax.text(5.0, 0.75, note, fontsize=9.5, fontweight='bold', color=C_TEXT_MUTED, ha='center', fontstyle='italic')

        if idx == 0:
            # (1) Single Agent
            p = FancyBboxPatch((2.8, 4.0), 4.4, 1.8, boxstyle="round,pad=0.08,rounding_size=0.2", linewidth=1.5, edgecolor=C_SAGE, facecolor='#EBF2EE')
            ax.add_patch(p)
            ax.text(5.0, 4.9, "Single Agent", fontsize=13.0, fontweight='bold', color=C_SAGE, ha='center', va='center')
            ax.annotate("", xy=(2.8, 5.6), xytext=(2.8, 4.2), arrowprops=dict(arrowstyle='-|>,head_width=0.3,head_length=0.4', lw=1.6, color=C_SLATE, connectionstyle="arc3,rad=-1.25"))
            ax.text(1.2, 4.9, "Act ->\nObserve", fontsize=10.5, fontweight='bold', color=C_TEXT_DARK, ha='center')

        elif idx == 1:
            # (2) Sequential
            p_parent = FancyBboxPatch((2.6, 5.8), 4.8, 1.5, boxstyle="round,pad=0.08,rounding_size=0.2", linewidth=1.5, edgecolor=C_TERRA, facecolor='#FBEFEA')
            p_child = FancyBboxPatch((2.6, 2.2), 4.8, 1.5, boxstyle="round,pad=0.08,rounding_size=0.2", linewidth=1.5, edgecolor=C_SAGE, facecolor='#EBF2EE')
            ax.add_patch(p_parent); ax.add_patch(p_child)
            ax.text(5.0, 6.55, "Parent (Blocks)", fontsize=12.0, fontweight='bold', color=C_TERRA, ha='center', va='center')
            ax.text(5.0, 2.95, "Sub-agent (Single)", fontsize=12.0, fontweight='bold', color=C_SAGE, ha='center', va='center')
            ax.annotate("", xy=(4.0, 3.7), xytext=(4.0, 5.8), arrowprops=arr)
            ax.annotate("", xy=(6.0, 5.8), xytext=(6.0, 3.7), arrowprops=arr_dashed)
            ax.text(3.1, 4.75, "task", fontsize=10.0, fontweight='bold', color=C_TEXT_MUTED)
            ax.text(6.3, 4.75, "summary", fontsize=10.0, fontweight='bold', color=C_TEXT_MUTED)

        elif idx == 2:
            # (3) Parallel Child Sessions
            p_parent = FancyBboxPatch((2.8, 6.2), 4.4, 1.5, boxstyle="round,pad=0.08,rounding_size=0.2", linewidth=1.5, edgecolor=C_TERRA, facecolor='#FBEFEA')
            p_s1 = FancyBboxPatch((0.8, 2.4), 3.8, 1.5, boxstyle="round,pad=0.08,rounding_size=0.2", linewidth=1.5, edgecolor=C_SLATE, facecolor='#EBF0F5')
            p_s2 = FancyBboxPatch((5.4, 2.4), 3.8, 1.5, boxstyle="round,pad=0.08,rounding_size=0.2", linewidth=1.5, edgecolor=C_SLATE, facecolor='#EBF0F5')
            ax.add_patch(p_parent); ax.add_patch(p_s1); ax.add_patch(p_s2)
            ax.text(5.0, 6.95, "Parent Session", fontsize=12.0, fontweight='bold', color=C_TERRA, ha='center', va='center')
            ax.text(2.7, 3.15, "Session A", fontsize=11.5, fontweight='bold', color=C_SLATE, ha='center', va='center')
            ax.text(7.3, 3.15, "Session B", fontsize=11.5, fontweight='bold', color=C_SLATE, ha='center', va='center')
            ax.annotate("", xy=(2.7, 3.9), xytext=(4.2, 6.2), arrowprops=arr)
            ax.annotate("", xy=(7.3, 3.9), xytext=(5.8, 6.2), arrowprops=arr)

        elif idx == 3:
            # (4) Hierarchical Thread Tree
            p_root = FancyBboxPatch((3.0, 6.8), 4.0, 1.3, boxstyle="round,pad=0.06,rounding_size=0.18", linewidth=1.5, edgecolor=C_TERRA, facecolor='#FBEFEA')
            p_t1 = FancyBboxPatch((1.0, 4.4), 3.5, 1.2, boxstyle="round,pad=0.06,rounding_size=0.18", linewidth=1.4, edgecolor=C_SAGE, facecolor='#EBF2EE')
            p_t2 = FancyBboxPatch((5.5, 4.4), 3.5, 1.2, boxstyle="round,pad=0.06,rounding_size=0.18", linewidth=1.4, edgecolor=C_SAGE, facecolor='#EBF2EE')
            p_sub = FancyBboxPatch((5.5, 2.0), 3.5, 1.1, boxstyle="round,pad=0.06,rounding_size=0.18", linewidth=1.4, edgecolor=C_SLATE, facecolor='#EBF0F5')
            ax.add_patch(p_root); ax.add_patch(p_t1); ax.add_patch(p_t2); ax.add_patch(p_sub)
            ax.text(5.0, 7.45, "Root Thread", fontsize=11.5, fontweight='bold', color=C_TERRA, ha='center', va='center')
            ax.text(2.75, 5.0, "Branch A", fontsize=11.0, fontweight='bold', color=C_SAGE, ha='center', va='center')
            ax.text(7.25, 5.0, "Branch B", fontsize=11.0, fontweight='bold', color=C_SAGE, ha='center', va='center')
            ax.text(7.25, 2.55, "Sub-branch ...", fontsize=10.5, fontweight='bold', color=C_SLATE, ha='center', va='center')
            ax.annotate("", xy=(2.75, 5.6), xytext=(4.0, 6.8), arrowprops=arr)
            ax.annotate("", xy=(7.25, 5.6), xytext=(6.0, 6.8), arrowprops=arr)
            ax.annotate("", xy=(7.25, 3.1), xytext=(7.25, 4.4), arrowprops=arr)

        elif idx == 4:
            # (5) Recursive Composition
            p_a1 = FancyBboxPatch((3.0, 6.8), 4.0, 1.25, boxstyle="round,pad=0.06,rounding_size=0.18", linewidth=1.5, edgecolor=C_TERRA, facecolor='#FBEFEA')
            p_a2 = FancyBboxPatch((3.0, 4.4), 4.0, 1.25, boxstyle="round,pad=0.06,rounding_size=0.18", linewidth=1.4, edgecolor=C_SAGE, facecolor='#EBF2EE')
            p_a3 = FancyBboxPatch((3.0, 2.0), 4.0, 1.25, boxstyle="round,pad=0.06,rounding_size=0.18", linewidth=1.4, edgecolor=C_OCHRE, facecolor='#F9F5EC')
            ax.add_patch(p_a1); ax.add_patch(p_a2); ax.add_patch(p_a3)
            ax.text(5.0, 7.42, "Agent (Parent)", fontsize=11.5, fontweight='bold', color=C_TERRA, ha='center', va='center')
            ax.text(5.0, 5.02, "Sub-agent (Child)", fontsize=11.5, fontweight='bold', color=C_SAGE, ha='center', va='center')
            ax.text(5.0, 2.62, "Sub-sub-agent", fontsize=11.5, fontweight='bold', color=C_OCHRE, ha='center', va='center')
            ax.annotate("", xy=(5.0, 5.65), xytext=(5.0, 6.8), arrowprops=arr)
            ax.annotate("", xy=(5.0, 3.25), xytext=(5.0, 4.4), arrowprops=arr)
            ax.text(7.2, 6.1, "fork ctx", fontsize=10.0, fontweight='bold', color=C_TEXT_MUTED)
            ax.text(7.2, 3.7, "fork ctx", fontsize=10.0, fontweight='bold', color=C_TEXT_MUTED)

        elif idx == 5:
            # (6) Registry + Protocol
            p_p = FancyBboxPatch((0.8, 4.4), 2.8, 1.7, boxstyle="round,pad=0.06,rounding_size=0.18", linewidth=1.5, edgecolor=C_TERRA, facecolor='#FBEFEA')
            p_reg = FancyBboxPatch((4.0, 4.4), 2.8, 1.7, boxstyle="round,pad=0.06,rounding_size=0.18", linewidth=1.4, edgecolor=C_SAGE, facecolor='#EBF2EE')
            p_rem = FancyBboxPatch((7.2, 4.4), 2.5, 1.7, boxstyle="round,pad=0.06,rounding_size=0.18", linewidth=1.4, edgecolor=C_SLATE, facecolor='#EBF0F5')
            ax.add_patch(p_p); ax.add_patch(p_reg); ax.add_patch(p_rem)
            ax.text(2.2, 5.25, "Parent Agent", fontsize=11.0, fontweight='bold', color=C_TERRA, ha='center', va='center')
            ax.text(5.4, 5.45, "Registry", fontsize=11.5, fontweight='bold', color=C_SAGE, ha='center')
            ax.text(5.4, 4.95, "(Agent defs)", fontsize=9.5, fontweight='bold', color=C_TEXT_MUTED, ha='center')
            ax.text(8.45, 5.45, "Remote Agent", fontsize=11.0, fontweight='bold', color=C_SLATE, ha='center')
            ax.text(8.45, 4.95, "(A2A/ACP)", fontsize=9.5, fontweight='bold', color=C_TEXT_MUTED, ha='center')
            ax.annotate("", xy=(4.0, 5.25), xytext=(3.6, 5.25), arrowprops=arr)
            ax.annotate("", xy=(7.2, 5.25), xytext=(6.8, 5.25), arrowprops=arr)
            ax.plot([7.0, 7.0], [1.5, 8.5], ls='--', color=C_BORDER_DARK, lw=1.5)
            ax.text(7.0, 8.7, "Process Boundary", fontsize=10.0, fontweight='bold', color=C_TEXT_MUTED, ha='center')

    plt.tight_layout()
    plt.savefig('fig6_matplotlib.png', dpi=300, facecolor=C_CANVAS)
    plt.close()
    print("Successfully generated fig6_matplotlib.png with enlarged text")

if __name__ == '__main__':
    draw_figure_1()
    draw_figure_2()
    draw_figure_6()
