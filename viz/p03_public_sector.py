"""
Project 03: Public Sector Descriptive Analysis
Visualisations: Demographic Shift, Policy Impact Timeline
"""

import matplotlib.pyplot as plt
import seaborn as sns
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

def plot_demographic_shift():
    """Population Pyramid for Demographic Shift Analysis"""
    age_groups = ['0-9', '10-19', '20-29', '30-39', '40-49', '50-59', '60-69', '70-79', '80+']
    
    # 2010 Data
    pop_2010 = np.array([5.2, 5.8, 6.5, 6.2, 5.5, 4.8, 3.5, 2.1, 1.0])
    # 2020 Data (Aging population shift)
    pop_2020 = np.array([4.8, 5.3, 6.0, 6.8, 6.1, 5.4, 4.5, 3.0, 1.8])
    
    y = np.arange(len(age_groups))
    
    fig, ax = plt.subplots(figsize=(8, 6))
    
    # Plot 2010 as lines/outlines
    ax.barh(y, pop_2010, height=0.5, color='none', edgecolor=TEXT_SECONDARY, linestyle='--', linewidth=1.5, label='2010 Baseline')
    
    # Plot 2020 as solid bars
    ax.barh(y, pop_2020, height=0.5, color=CYAN, alpha=0.8, label='2020 Actual')
    
    ax.set_yticks(y)
    ax.set_yticklabels(age_groups)
    ax.set_xlabel("Population (%)")
    ax.set_title("DECADE DEMOGRAPHIC SHIFT (2010 vs 2020)", pad=20, fontdict={'weight': 'bold'})
    ax.grid(axis='x', linestyle='--')
    
    ax.legend(facecolor=SURFACE_COLOR, edgecolor="#2A2D3D")
    
    plt.tight_layout()
    return fig

def plot_service_utilization():
    """Service Utilization Heatmap across Demographics"""
    services = ['Healthcare', 'Education', 'Transport', 'Social Care', 'Housing']
    demographics = ['Low Income', 'Middle Income', 'High Income', 'Retirees', 'Students']
    
    # Mock utilization matrix
    data = np.array([
        [8.5, 6.2, 7.8, 4.1, 9.2],  # Healthcare
        [4.2, 8.9, 9.5, 1.2, 2.5],  # Education
        [7.8, 6.5, 4.2, 8.5, 5.1],  # Transport
        [9.1, 3.2, 1.5, 9.8, 4.5],  # Social Care
        [6.5, 4.8, 2.1, 7.5, 8.2]   # Housing
    ])
    
    fig, ax = plt.subplots(figsize=(8, 6))
    
    sns.heatmap(data, cmap=sns.dark_palette(CYAN, as_cmap=True), 
                xticklabels=demographics, yticklabels=services,
                linewidths=1, linecolor=BG_COLOR, ax=ax, cbar_kws={'label': 'Utilization Index'})
    
    ax.set_title("SERVICE UTILIZATION MATRIX", pad=20, fontdict={'weight': 'bold'})
    
    plt.tight_layout()
    return fig

if __name__ == "__main__":
    fig1 = plot_demographic_shift()
    fig2 = plot_service_utilization()
    plt.show()
