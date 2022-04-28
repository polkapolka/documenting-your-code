"""
random color palette
"""
import matplotlib.pyplot as plt
import requests


def plot_palette(model: str) -> plt.Figure:
    """Return a series of colors for use as a palette with the

    Args:
        model: "default" or "ui"

    Returns: Figure with set color palette.

    """
    if model not in {"default", "ui"}:
        raise ValueError(f"{model} is not supported.")

    data = f'{{"model": "{model}"}}'

    response = requests.post("http://colormind.io/api/", data=data)
    palette = response.json()

    fig, axs = plt.subplots(figsize=(10, 2), nrows=1, ncols=5)

    for idx, color in enumerate(palette["result"]):
        color_decimal = [val / 256 for val in color]
        axs[idx].set_facecolor(color_decimal)

        axs[idx].set_title(color)
        axs[idx].set_xticks([])
        axs[idx].set_yticks([])

    return fig
