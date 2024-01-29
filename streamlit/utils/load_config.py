from typing import Dict
import tomli


def load_theme() -> Dict:
    with open(".streamlit/config.toml", "rb") as f:
        config = tomli.load(f)

    theme = config["theme"]

    return theme
