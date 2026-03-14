import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
from pydantic import BaseModel

class DataPoint(BaseModel):
    mean: float
    lower: float
    upper: float

def plot(
    data: list[DataPoint],
    x: list[float],
    x_title: str,
    y_title: str,
    title: str = "",
) -> plt.Figure:
    means  = [d.mean  for d in data]
    lowers = [d.lower for d in data]
    uppers = [d.upper for d in data]

    green      = "#2e7d32"
    green_fill = "#a5d6a7"

    with sns.axes_style("whitegrid"):
        fig, ax = plt.subplots(figsize=(10, 6))

        ax.fill_between(x, lowers, uppers, color=green_fill, alpha=0.5,
                        label="25th-75th Percentile Range")
        ax.plot(x, means, color=green, marker="o", linewidth=2,
                markersize=6, label="Median Time")

        ax.set_xlabel(x_title, fontsize=12)
        ax.set_ylabel(y_title, fontsize=12)
        ax.set_title(title, fontsize=13, fontweight="bold")
        ax.set_xticks(x)
        ax.grid(axis="both", linestyle="--", alpha=0.6)
        ax.legend(frameon=True, fontsize=10)

        plt.tight_layout()
        fig.savefig("plot.png", dpi=150, bbox_inches="tight")
    return fig


if __name__ == '__main__':
    data = [DataPoint(mean=i, lower=0.2*i*i, upper=1 + i**2) for i in range(20)]
    plot(data, "x", "y", "title")