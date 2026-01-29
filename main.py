# main.py
from src.parse import parse_all_demos
from src.spatial import normalize_coordinates
from src.heatmaps import plot_heatmap
from src.tactics import cluster_positions
from src.features import build_round_features
from src.maps import map_config

# 1. Parse
kills, ticks = parse_all_demos("demos/timeX")

# 2. Spatial
map_cfg = map_config["de_dust2"]
ticks = normalize_coordinates(ticks, map_cfg)

# 3. Visualização
plot_heatmap(ticks, "Movimentação - Team X")
plot_heatmap(kills, "Kills - Team X")

# 4. Tática
ticks = cluster_positions(ticks)

# 5. Features
features_df = build_round_features(ticks)
features_df.to_csv("data/features/team_x_rounds.csv", index=False)