# main.py

from src.parse import parse_all_demos
from src.spatial import normalize_coordinates
from src.heatmaps import plot_heatmap
from src.tactics import cluster_positions
from src.features import build_round_features
from src.maps import map_config

# =========================
# CONFIGURAÇÕES
# =========================
DEMO_DIR = "demos/timeX"
MAP_NAME = "de_dust2"

# =========================
# 1. PARSE DOS DEMOS
# =========================
kills, ticks = parse_all_demos(DEMO_DIR)

print("Parse concluído")
print("Kills:", kills.shape)
print("Ticks:", ticks.shape)

# =========================
# 2. NORMALIZAÇÃO ESPACIAL
# =========================
map_cfg = map_config[MAP_NAME]
ticks = normalize_coordinates(ticks, map_cfg)

# Ajuste comum de coordenadas 
ticks["y_norm"] = 1 - ticks["y_norm"]

print("Normalização espacial concluída")

# =========================
# 3. VISUALIZAÇÃO (MAPA + HEATMAP)
# =========================
plot_heatmap(
    ticks,
    title="Movimentação Geral - Team X",
    max_points=120_000,
)

# =========================
# 4. ANÁLISE TÁTICA (CLUSTERS)
# =========================
ticks = cluster_positions(ticks, k=6)

print("Clusterização tática concluída")
print(ticks["cluster"].value_counts())

# =========================
# 5. FEATURES PARA ML
# =========================
features_df = build_round_features(ticks)

features_df.to_csv(
    "data/features/team_x_rounds.csv",
    index=False
)

print("Features geradas com sucesso")
print(features_df.head())
