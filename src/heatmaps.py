# src/heatmaps.py
import matplotlib.pyplot as plt
import numpy as np


def plot_heatmap(
    df,
    title,
    bins=80,
    max_points=500_000
):
    if len(df) == 0:
        print("DataFrame vazio. Heatmap não gerado.")
        return

    if len(df) > max_points:
        df = df.sample(n=max_points, random_state=42)

    plt.figure(figsize=(6, 6), facecolor="white")

    # Histograma 2D
    heatmap, xedges, yedges = np.histogram2d(
        df["x_norm"],
        df["y_norm"],
        bins=bins,
        range=[[0, 1], [0, 1]]
    )

    # Mascarar regiões sem dados
    heatmap = np.ma.masked_where(heatmap == 0, heatmap)

    plt.imshow(
        heatmap.T,
        origin="lower",
        cmap="Reds",
        extent=[0, 1, 0, 1],
        aspect="auto"
    )

    plt.colorbar(label="Densidade")
    plt.title(title)
    plt.xlabel("X normalizado")
    plt.ylabel("Y normalizado")
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.gca().set_facecolor("white")

    plt.tight_layout()
    plt.show()
