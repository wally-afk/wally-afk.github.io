"""
Project 01: Olist E-Commerce Intelligence
Visualisations: Revenue Heatmap, Review Paradox, Payment Breakdown, Delivery Distribution
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# ─── DESIGN TOKENS (Swiss Minimalist Portfolio) ──────────────
BG_COLOR = "#090A0F"
CARD_COLOR = "#12131A"
SURFACE_COLOR = "#171922"
CYAN = "#06B6D4"
EMERALD = "#10B981"
TEXT_PRIMARY = "#F5F7FA"
TEXT_SECONDARY = "#8B909B"
BORDER = "rgba(255,255,255,0.08)"

# Apply global styling
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
    "font.family": "monospace",
    "font.monospace": ["JetBrains Mono", "Consolas", "Courier New", "monospace"]
})

def plot_revenue_heatmap():
    """1. Revenue Heatmap (Day of Week vs Hour of Day)"""
    # Mocking data to reflect weekday afternoon clustering
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    hours = [f"{h:02d}:00" for h in range(8, 22)]
    
    # Generate base noise
    data = np.random.uniform(10, 40, size=(len(days), len(hours)))
    
    # Add peak clusters (weekday afternoons)
    for i in range(5):  # Mon-Fri
        for j in range(4, 10):  # 12:00 - 17:00
            data[i, j] += np.random.uniform(50, 90)
            
    df = pd.DataFrame(data, index=days, columns=hours)
    
    fig, ax = plt.subplots(figsize=(10, 4))
    
    # Custom cyan colormap
    cmap = sns.dark_palette(CYAN, as_cmap=True)
    cmap.set_under(CARD_COLOR)
    
    sns.heatmap(df, cmap=cmap, linewidths=0.5, linecolor=BG_COLOR, 
                cbar_kws={"shrink": 0.8}, ax=ax)
    
    ax.set_title("REVENUE CLUSTERING (Day vs Hour)", pad=20, fontdict={'fontname': 'Inter', 'weight': 'bold'})
    ax.set_xlabel("Hour of Day")
    ax.set_ylabel("Day of Week")
    
    plt.tight_layout()
    return fig

def plot_review_paradox():
    """2. The Review Paradox (Sales Volume vs Avg Review Score)"""
    # Mocking data
    np.random.seed(42)
    categories = [f"Cat_{i}" for i in range(40)]
    
    # High volume, average scores (3.8 - 4.2)
    vol_main = np.random.normal(5000, 1500, 30)
    score_main = np.random.normal(4.0, 0.2, 30)
    
    # Low volume, high scores (4.6 - 5.0) - The Paradox
    vol_niche = np.random.normal(300, 150, 10)
    score_niche = np.random.normal(4.8, 0.15, 10)
    
    volumes = np.concatenate([vol_main, vol_niche])
    scores = np.concatenate([score_main, score_niche])
    
    # Cap scores at 5.0
    scores = np.clip(scores, 1.0, 5.0)
    volumes = np.clip(volumes, 50, None)
    
    fig, ax = plt.subplots(figsize=(8, 5))
    
    # Main categories
    ax.scatter(volumes[:30], scores[:30], color=TEXT_SECONDARY, alpha=0.5, s=50, label="High Volume / Avg Score")
    # Paradox categories
    ax.scatter(volumes[30:], scores[30:], color=EMERALD, alpha=0.8, s=80, edgecolor=BG_COLOR, label="Low Volume / High Score")
    
    ax.set_title("THE REVIEW PARADOX", pad=20, fontdict={'fontname': 'Inter', 'weight': 'bold'})
    ax.set_xlabel("Total Sales Volume")
    ax.set_ylabel("Average Review Score (1-5)")
    ax.grid(True, linestyle="--")
    
    # Highlight area
    ax.axvspan(0, 1000, ymin=0.8, ymax=1.0, color=EMERALD, alpha=0.05)
    ax.text(250, 4.9, "Niche Excellence", color=EMERALD, fontsize=9, ha='center')
    
    ax.legend(facecolor=SURFACE_COLOR, edgecolor="#2A2D3D", labelcolor=TEXT_PRIMARY)
    
    plt.tight_layout()
    return fig

def plot_payment_breakdown():
    """3. Payment Breakdown (Donut Chart)"""
    labels = ["Credit Card", "Boleto", "Voucher", "Debit Card"]
    sizes = [75.34, 19.5, 3.8, 1.36]
    
    # Colors: Highlight Credit Card with Cyan, others muted
    colors = [CYAN, "#2A2D3D", "#1C1F2A", SURFACE_COLOR]
    
    fig, ax = plt.subplots(figsize=(6, 6))
    
    wedges, texts, autotexts = ax.pie(
        sizes, 
        labels=labels, 
        colors=colors, 
        autopct='%1.1f%%',
        startangle=90, 
        pctdistance=0.85,
        wedgeprops=dict(width=0.3, edgecolor=BG_COLOR, linewidth=2),
        textprops=dict(color=TEXT_PRIMARY)
    )
    
    # Style the text
    for i, autotext in enumerate(autotexts):
        autotext.set_color(BG_COLOR if i == 0 else TEXT_PRIMARY)
        autotext.set_fontweight("bold")
        
    for text in texts:
        text.set_color(TEXT_SECONDARY)
        
    # Center text
    ax.text(0, 0.05, "75.34%", ha='center', va='center', fontsize=24, fontweight='bold', color=CYAN)
    ax.text(0, -0.15, "CREDIT CARD", ha='center', va='center', fontsize=10, color=TEXT_SECONDARY)
    
    ax.set_title("PAYMENT METHOD DISTRIBUTION", pad=20, fontdict={'fontname': 'Inter', 'weight': 'bold'})
    
    plt.tight_layout()
    return fig

def plot_delivery_distribution():
    """4. Delivery Distribution (Histogram)"""
    # Mocking skewed distribution for delivery times
    np.random.seed(42)
    # Right-skewed distribution (log-normal)
    delivery_times = np.random.lognormal(mean=2.3, sigma=0.6, size=5000)
    # Shift slightly and clip to realistic bounds (1 to 40 days)
    delivery_times = np.clip(delivery_times, 1, 40)
    
    mean_delivery = 12.09 # Hardcoded from verified data
    
    fig, ax = plt.subplots(figsize=(8, 4))
    
    # Histogram
    n, bins, patches = ax.hist(delivery_times, bins=30, color=SURFACE_COLOR, edgecolor="#2A2D3D")
    
    # Mean reference line
    ax.axvline(mean_delivery, color=CYAN, linestyle='--', linewidth=2)
    
    # Annotation for mean
    ax.text(mean_delivery + 1, ax.get_ylim()[1] * 0.9, f"Mean: {mean_delivery} days", 
            color=CYAN, fontweight='bold', fontsize=10)
    
    ax.set_title("DELIVERY TIME DISTRIBUTION", pad=20, fontdict={'fontname': 'Inter', 'weight': 'bold'})
    ax.set_xlabel("Days to Deliver")
    ax.set_ylabel("Number of Orders")
    ax.grid(True, linestyle="--", axis='y')
    
    plt.tight_layout()
    return fig

if __name__ == "__main__":
    fig1 = plot_revenue_heatmap()
    fig2 = plot_review_paradox()
    fig3 = plot_payment_breakdown()
    fig4 = plot_delivery_distribution()
    
    plt.show()
