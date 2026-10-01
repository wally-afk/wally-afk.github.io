"""
Project 05: Olive Oil Market Research
Visualisations: Conjoint Analysis Utility Scores, Market Segment Radar
"""

import matplotlib.pyplot as plt
import numpy as np

# ─── DESIGN TOKENS ──────────────
BG_COLOR = "#090A0F"
CARD_COLOR = "#12131A"
SURFACE_COLOR = "#171922"
CYAN = "#06B6D4"
EMERALD = "#10B981"
TEXT_PRIMARY = "#F5F7FA"
TEXT_SECONDARY = "#8B909B"

plt.rcParams.update({
    "figure.facecolor": BG_COLOR,
    "axes.facecolor": CARD_COLOR,
    "axes.edgecolor": "#2A2D3D",
    "axes.labelcolor": TEXT_SECONDARY,
    "text.color": TEXT_PRIMARY,
    "xtick.color": TEXT_SECONDARY,
    "ytick.color": TEXT_SECONDARY,
    "grid.color": "#1C1F2A",
    "grid.alpha": 0.5,
    "font.family": "monospace"
})

def plot_conjoint_utilities():
    """Bar chart showing relative importance of attributes (Conjoint Analysis)"""
    attributes = ['Origin (Italy)', 'Origin (Spain)', 'Origin (Greece)', 
                  'Price (€15)', 'Price (€25)', 'Price (€35)',
                  'Cert (Organic)', 'Cert (DOP)', 'Cert (None)',
                  'Taste (Fruity)', 'Taste (Robust)']
    
    utilities = [1.2, 0.5, 0.2, 2.5, 0.5, -2.1, 1.8, 1.5, -0.8, 0.9, 0.4]
    
    # Colors based on positive/negative utility
    colors = [CYAN if u > 0 else "#EF4444" for u in utilities]
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    y_pos = np.arange(len(attributes))
    ax.barh(y_pos, utilities, color=colors, edgecolor=BG_COLOR)
    
    ax.set_yticks(y_pos)
    ax.set_yticklabels(attributes)
    ax.set_xlabel("Part-Worth Utility Score")
    ax.set_title("CONJOINT ANALYSIS: ATTRIBUTE UTILITIES", pad=20, fontdict={'weight': 'bold'})
    
    ax.axvline(0, color=TEXT_SECONDARY, linewidth=1)
    ax.grid(axis='x', linestyle='--')
    
    plt.tight_layout()
    return fig

def plot_segment_radar():
    """Radar chart for consumer segment preferences"""
    categories = ['Price Sensitivity', 'Brand Loyalty', 'Quality Focus', 'Health Consciousness', 'Packaging Importance']
    N = len(categories)
    
    # Values for two segments
    segment_value = [8, 4, 9, 7, 5]
    segment_budget = [2, 8, 4, 3, 4]
    
    # Angle calculation
    angles = [n / float(N) * 2 * np.pi for n in range(N)]
    angles += angles[:1]
    
    # Append first value to close the circle
    segment_value += segment_value[:1]
    segment_budget += segment_budget[:1]
    
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
    ax.set_facecolor(CARD_COLOR)
    
    # Draw Value Segment
    ax.plot(angles, segment_value, linewidth=2, linestyle='solid', color=EMERALD, label='Premium Segment')
    ax.fill(angles, segment_value, color=EMERALD, alpha=0.25)
    
    # Draw Budget Segment
    ax.plot(angles, segment_budget, linewidth=2, linestyle='solid', color=CYAN, label='Value Segment')
    ax.fill(angles, segment_budget, color=CYAN, alpha=0.25)
    
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories)
    
    ax.set_rlabel_position(0)
    ax.set_yticks([2, 4, 6, 8])
    ax.set_yticklabels(["2", "4", "6", "8"], color=TEXT_SECONDARY, size=8)
    ax.set_ylim(0, 10)
    
    ax.set_title("CONSUMER SEGMENT PROFILES", pad=30, fontdict={'weight': 'bold'})
    ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), facecolor=SURFACE_COLOR, edgecolor="#2A2D3D")
    
    plt.tight_layout()
    return fig

if __name__ == "__main__":
    fig1 = plot_conjoint_utilities()
    fig2 = plot_segment_radar()
    plt.show()
