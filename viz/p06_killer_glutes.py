"""
Project 06: Killer Glute Bikes BI
Visualisations: Sales Funnel, Customer Retention Cohort Analysis
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from matplotlib.patches import Polygon

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

def plot_sales_funnel():
    """Sales Funnel Visualization"""
    stages = ['Website Visits', 'Product Views', 'Add to Cart', 'Checkout', 'Purchase']
    values = [100000, 45000, 15000, 8000, 3500]
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_facecolor(BG_COLOR)
    
    y = np.arange(len(stages))[::-1]  # Reverse for top-to-bottom
    
    # Calculate widths for the funnel effect
    max_val = max(values)
    widths = [v / max_val for v in values]
    
    # Custom color gradient
    colors = sns.dark_palette(CYAN, n_colors=len(stages), reverse=True)
    
    for i, (val, width, color) in enumerate(zip(values, widths, colors)):
        # Calculate polygon points
        left = -width/2
        right = width/2
        
        # Next width for the bottom of the polygon (if not last)
        next_width = widths[i+1] if i < len(widths)-1 else width * 0.8
        next_left = -next_width/2
        next_right = next_width/2
        
        # Y coordinates
        top_y = y[i] + 0.4
        bot_y = y[i] - 0.4
        
        verts = [(left, top_y), (right, top_y), (next_right, bot_y), (next_left, bot_y)]
        poly = Polygon(verts, facecolor=color, edgecolor=BG_COLOR, linewidth=2)
        ax.add_patch(poly)
        
        # Add value text
        ax.text(0, y[i], f"{val:,}\n({val/values[0]:.1%})", ha='center', va='center', 
                color=TEXT_PRIMARY, fontweight='bold')
        
    ax.set_yticks(y)
    ax.set_yticklabels(stages, fontweight='bold')
    ax.set_xlim(-0.6, 0.6)
    ax.set_xticks([])
    
    # Remove borders
    for spine in ax.spines.values():
        spine.set_visible(False)
        
    ax.set_title("E-COMMERCE CONVERSION FUNNEL", pad=20, fontdict={'weight': 'bold'})
    
    plt.tight_layout()
    return fig

def plot_cohort_analysis():
    """Customer Retention Cohort Analysis (Heatmap)"""
    np.random.seed(42)
    
    # Generate mock cohort data (retention rates)
    cohorts = [f"2023-M{i:02d}" for i in range(1, 13)]
    months_active = list(range(1, 13))
    
    data = np.zeros((12, 12))
    
    for i in range(12):
        # Month 1 is always 100%
        data[i, 0] = 100.0
        # Decay function for retention
        for j in range(1, 12-i):
            decay = np.random.uniform(0.7, 0.85) if j == 1 else np.random.uniform(0.85, 0.95)
            data[i, j] = data[i, j-1] * decay
            
    # Mask the lower triangle (future months)
    mask = np.zeros_like(data)
    for i in range(12):
        for j in range(12-i, 12):
            mask[i, j] = 1
            data[i, j] = np.nan
            
    df = pd.DataFrame(data, index=cohorts, columns=months_active)
    
    fig, ax = plt.subplots(figsize=(12, 8))
    
    sns.heatmap(df, mask=mask, cmap=sns.dark_palette(EMERALD, as_cmap=True),
                annot=True, fmt=".1f", cbar_kws={'label': 'Retention Rate (%)'},
                linewidths=1, linecolor=BG_COLOR, ax=ax)
    
    ax.set_title("CUSTOMER RETENTION BY MONTHLY COHORT", pad=20, fontdict={'weight': 'bold'})
    ax.set_xlabel("Months Since First Purchase")
    ax.set_ylabel("Acquisition Cohort")
    
    plt.tight_layout()
    return fig

if __name__ == "__main__":
    fig1 = plot_sales_funnel()
    fig2 = plot_cohort_analysis()
    plt.show()
