"""
Project 04: PLS-SEM Marketing
Visualisations: Path Model Coefficients, Construct Reliability
"""

import matplotlib.pyplot as plt
import networkx as nx
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
    "axes.facecolor": BG_COLOR,
    "text.color": TEXT_PRIMARY,
    "font.family": "monospace"
})

def plot_sem_path_model():
    """Network graph representing the PLS-SEM structural model"""
    G = nx.DiGraph()
    
    # Add nodes (Latent Constructs)
    constructs = ["Brand\nAwareness", "Perceived\nQuality", "Brand\nLoyalty", "Purchase\nIntention"]
    for c in constructs:
        G.add_node(c)
        
    # Add edges with path coefficients (weights)
    edges = [
        ("Brand\nAwareness", "Perceived\nQuality", 0.65),
        ("Brand\nAwareness", "Brand\nLoyalty", 0.32),
        ("Perceived\nQuality", "Brand\nLoyalty", 0.58),
        ("Brand\nLoyalty", "Purchase\nIntention", 0.72),
        ("Perceived\nQuality", "Purchase\nIntention", 0.45)
    ]
    
    for u, v, w in edges:
        G.add_edge(u, v, weight=w)
        
    # Define fixed layout for clarity
    pos = {
        "Brand\nAwareness": (-1, 1),
        "Perceived\nQuality": (1, 1),
        "Brand\nLoyalty": (0, 0),
        "Purchase\nIntention": (0, -1)
    }
    
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Draw nodes
    nx.draw_networkx_nodes(G, pos, ax=ax, node_size=6000, node_color=CARD_COLOR, 
                           edgecolors=CYAN, linewidths=2, node_shape="s")
    
    # Draw edges
    weights = [G[u][v]['weight'] * 5 for u,v in G.edges()]
    nx.draw_networkx_edges(G, pos, ax=ax, arrowsize=20, width=weights, edge_color=TEXT_SECONDARY, 
                           connectionstyle="arc3,rad=0.1")
    
    # Draw labels
    nx.draw_networkx_labels(G, pos, ax=ax, font_size=10, font_family="monospace", font_color=TEXT_PRIMARY)
    
    # Draw edge labels (Path coefficients)
    edge_labels = {(u, v): f"β={w}" for u, v, w in edges}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, ax=ax, font_color=EMERALD, font_family="monospace")
    
    ax.set_title("STRUCTURAL EQUATION MODEL (PLS-SEM)", pad=20, fontdict={'weight': 'bold'})
    ax.axis('off')
    
    plt.tight_layout()
    return fig

def plot_reliability_metrics():
    """Bar chart for Cronbach's Alpha and Composite Reliability"""
    constructs = ['Brand Awareness', 'Perceived Quality', 'Brand Loyalty', 'Purchase Intention']
    cronbach = [0.82, 0.88, 0.91, 0.85]
    cr = [0.86, 0.92, 0.94, 0.89]
    
    x = np.arange(len(constructs))
    width = 0.35
    
    fig, ax = plt.subplots(figsize=(10, 5))
    
    # Re-apply styling for this specific plot
    ax.set_facecolor(CARD_COLOR)
    ax.grid(axis='y', linestyle='--', color="#1C1F2A", alpha=0.5)
    
    ax.bar(x - width/2, cronbach, width, label="Cronbach's Alpha", color=SURFACE_COLOR, edgecolor=TEXT_SECONDARY)
    ax.bar(x + width/2, cr, width, label="Composite Reliability (CR)", color=CYAN, alpha=0.8)
    
    # Threshold line
    ax.axhline(y=0.7, color=EMERALD, linestyle='--', label="Acceptable Threshold (0.7)")
    
    ax.set_ylabel('Reliability Score')
    ax.set_title('CONSTRUCT RELIABILITY METRICS', pad=20, fontdict={'weight': 'bold'})
    ax.set_xticks(x)
    ax.set_xticklabels(constructs)
    ax.set_ylim(0, 1.1)
    
    ax.legend(facecolor=SURFACE_COLOR, edgecolor="#2A2D3D", loc='lower right')
    
    plt.tight_layout()
    return fig

if __name__ == "__main__":
    fig1 = plot_sem_path_model()
    fig2 = plot_reliability_metrics()
    plt.show()
