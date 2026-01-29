# src/tactics.py
from sklearn.cluster import KMeans
import pandas as pd

def cluster_positions(df, k=6):
    df = df.copy()
    X = df[["x_norm", "y_norm"]]
    model = KMeans(n_clusters=k, random_state=42)
    df["cluster"] = model.fit_predict(X)
    return df

def classify_round_phase(df):
    df = df.copy()
    df["phase"] = pd.cut(
        df["time"],
        bins=[0, 30, 70, 999],
        labels=["early", "mid", "late"]
    )
    return df