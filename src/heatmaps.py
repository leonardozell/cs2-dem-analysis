import matplotlib.pyplot as plt
import seaborn as sns

def plot_heatmap(df, title):
    plt.figure(figsize=(6, 6))
    sns.kdeplot(
        x=df["x_norm"],
        y=df["y_norm"],
        fill=True,
        cmap="Reds",
        thresh=0.05
    )
    plt.title(title)
    plt.axis("off")
    plt.show()
