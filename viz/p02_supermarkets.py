"""
Project 02: Retail Geography (Supermarket Optimization)
Visualisations: Geospatial Store Distribution, Catchment Area Overlap, Performance by Region
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

def plot_store_network():
    """Simulated geospatial map of store network with Voronoi-like catchment areas"""
    np.random.seed(101)
    
    # Store locations (simulated coordinates)
    x_stores = np.random.uniform(0, 100, 20)
    y_stores = np.random.uniform(0, 100, 20)
    
    # Store performance (size of point)
    performance = np.random.uniform(200, 1000, 20)
    
    fig, ax = plt.subplots(figsize=(8, 8))
    
    # Simulated Catchment Area Overlap (heat)
    x_grid, y_grid = np.meshgrid(np.linspace(0, 100, 100), np.linspace(0, 100, 100))
    z = np.zeros_like(x_grid)
    for i in range(len(x_stores)):
        z += np.exp(-((x_grid - x_stores[i])**2 + (y_grid - y_stores[i])**2) / 200)
    
    contour = ax.contourf(x_grid, y_grid, z, levels=15, cmap=sns.dark_palette(EMERALD, as_cmap=True), alpha=0.3)
    
    # Store points
    scatter = ax.scatter(x_stores, y_stores, s=performance, color=EMERALD, alpha=0.8, edgecolor=BG_COLOR, linewidth=1.5)
    
    # Highlight highest overlap areas (cannibalization risk)
    ax.contour(x_grid, y_grid, z, levels=[z.max()*0.8], colors=[CYAN], linewidths=2, linestyles='dashed')
    
    ax.set_title("STORE NETWORK & CATCHMENT OVERLAP", pad=20, fontdict={'weight': 'bold'})
    ax.set_xticks([])
    ax.set_yticks([])
    
    plt.tight_layout()
    return fig

def plot_regional_performance():
    """Performance by region bar chart"""
    regions = ['North', 'South', 'East', 'West', 'Central']
    revenue = [4.2, 3.8, 5.1, 2.9, 6.5] # Millions
    efficiency = [0.85, 0.92, 0.78, 0.88, 0.95] # Score 0-1
    
    fig, ax1 = plt.subplots(figsize=(10, 5))
    
    # Bar chart for revenue
    x = np.arange(len(regions))
    bars = ax1.bar(x, revenue, color=SURFACE_COLOR, edgecolor="#2A2D3D")
    bars[4].set_color(CYAN) # Highlight Central
    
    ax1.set_ylabel("Revenue (£ Millions)", color=TEXT_SECONDARY)
    ax1.set_xticks(x)
    ax1.set_xticklabels(regions)
    ax1.grid(axis='y', linestyle='--')
    
    # Line chart for efficiency on secondary axis
    ax2 = ax1.twinx()
    ax2.plot(x, efficiency, color=EMERALD, marker='o', linewidth=2, markersize=8)
    ax2.set_ylabel("Efficiency Score", color=EMERALD)
    ax2.set_ylim(0.5, 1.0)
    
    ax1.set_title("REGIONAL PERFORMANCE VS EFFICIENCY", pad=20, fontdict={'weight': 'bold'})
    
    plt.tight_layout()
    return fig

if __name__ == "__main__":
    fig1 = plot_store_network()
    fig2 = plot_regional_performance()
    plt.show()
