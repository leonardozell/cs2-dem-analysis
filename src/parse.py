# src/parse.py
from demoparser2 import DemoParser
from pathlib import Path
import pandas as pd

def parse_all_demos(demo_dir: str):
    all_kills = []
    all_ticks = []

    for demo_file in Path(demo_dir).glob("*.dem"):
        print("Lendo demo:", demo_file)

        demo = DemoParser(str(demo_file))  

        kills = demo.parse_event("player_death")
        ticks = demo.parse_ticks(
            wanted_props=["X", "Y", "Z", "m_iTeamNum", "tick", "round"]
        )

        kills["demo"] = demo_file.name
        ticks["demo"] = demo_file.name

        all_kills.append(kills)
        all_ticks.append(ticks)

    if not all_kills or not all_ticks:
        raise ValueError(
            "Nenhum .dem foi encontrado ou nenhum evento foi extraído."
        )

    return (
        pd.concat(all_kills, ignore_index=True),
        pd.concat(all_ticks, ignore_index=True)
    )