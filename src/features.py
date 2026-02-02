# src/features.py
import pandas as pd
from scipy.spatial.distance import pdist


def spread_per_tick(df_tick):
    """
    Spread do time em UM tick.
    """
    coords = df_tick[["x_norm", "y_norm"]].values

    if len(coords) < 2:
        return None

    return pdist(coords).mean()


def ensure_round_column(df):
    """
    Cria coluna 'round' usando saltos de tick.
    """
    if "round" in df.columns:
        return df

    if "tick" not in df.columns:
        raise ValueError("Coluna 'tick' é obrigatória")

    df = df.sort_values("tick").copy()

    df["round"] = (
        df["tick"]
        .diff()
        .fillna(0)
        .gt(5000)
        .cumsum()
    )

    return df


def build_round_features(ticks_df):
    """
    Features agregadas por round (forma correta).
    """
    df = ensure_round_column(ticks_df)

    round_features = []

    for round_id, df_round in df.groupby("round"):
        spreads = []

        for _, df_tick in df_round.groupby("tick"):
            s = spread_per_tick(df_tick)
            if s is not None:
                spreads.append(s)

        round_features.append({
            "round": int(round_id),
            "ticks": df_round["tick"].nunique(),
            "avg_spread": sum(spreads) / len(spreads) if spreads else 0.0
        })

    return pd.DataFrame(round_features)
