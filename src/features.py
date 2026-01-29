# src/features.py
import pandas as pd
from scipy.spatial.distance import pdist

def avg_team_spread(df_round):
    coords = df_round[["x_norm", "y_norm"]].values
    if len(coords) < 2:
        return 0
    return pdist(coords).mean()

def build_round_features(ticks_df):
    features = []

    for (demo, round_id), df_round in ticks_df.groupby(["demo", "round"]):
        spread = avg_team_spread(df_round)

        features.append({
            "demo": demo,
            "round": round_id,
            "avg_spread": spread
        })

    return pd.DataFrame(features)
