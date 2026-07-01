import json
from pathlib import Path
from streamlit_lottie import st_lottie

ASSETS = Path(__file__).parent / "assets"


def load_animation(filename):
    with open(ASSETS / filename, "r") as f:
        return json.load(f)


def shield():
    st_lottie(
        load_animation("shield.json"),
        speed=1,
        loop=True,
        height=220,
        key="shield"
    )


def loading():
    st_lottie(
        load_animation("loading.json"),
        speed=1,
        loop=True,
        height=160,
        key="loading"
    )