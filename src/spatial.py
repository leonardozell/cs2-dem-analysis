
def normalize_coordinates(df, map_cfg):
    required = {"X", "Y"}

    if not required.issubset(df.columns):
        raise ValueError(
            f"DataFrame não possui colunas necessárias: {required}"
        )

    df = df.copy()

    df["x_norm"] = (df["X"] - map_cfg["x_min"]) / (map_cfg["x_max"] - map_cfg["x_min"])
    df["y_norm"] = (df["Y"] - map_cfg["y_min"]) / (map_cfg["y_max"] - map_cfg["y_min"])

    return df