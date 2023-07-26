# flake8: noqa
import io

import IPython.display as display
import ipywidgets
import japanize_matplotlib
import matplotlib.figure
import matplotlib.pyplot as plt
from matplotlib.pyplot import *
from seaborn import kdeplot

plt.rcParams["figure.facecolor"] = "white"
plt.rcParams["mathtext.fontset"] = "cm"
plt.rcParams["pdf.fonttype"] = 42
plt.rcParams["figure.dpi"] = 100
plt.rcParams["axes.grid"] = True


def imshow(*args, **kwargs):
    im = plt.imshow(*args, **kwargs)
    plt.gca().grid(False)
    return im


def hbox_old(figures: list[matplotlib.figure.Figure], **kwargs):
    kwargs.setdefault("width", 400)
    widgets = []
    for fig in figures:
        buf = io.BytesIO()
        fig.savefig(buf, format="png")
        widgets.append(ipywidgets.Image(value=buf.getvalue(), format="png", **kwargs))
    display.display(ipywidgets.HBox(widgets))


class FigureBox:
    def __init__(self):
        self.figures = []

    def append(self, func=None, *args, **kwargs):
        if func is None:
            res = None
        else:
            res = func(*args, **kwargs)
        self.figures.append(plt.gcf())
        plt.close()
        return res

    def __iter__(self):
        yield from self.figures


class hbox:
    def __init__(self, **kwargs) -> None:
        self.kwargs = kwargs
        self.figures = FigureBox()

    def __enter__(self):
        return self.figures

    def __exit__(self, type, value, traceback):
        self.kwargs.setdefault("width", 400)
        widgets = []
        for fig in self.figures:
            buf = io.BytesIO()
            fig.savefig(buf, format="png")
            widgets.append(
                ipywidgets.Image(value=buf.getvalue(), format="png", **self.kwargs)
            )
        display.display(ipywidgets.HBox(widgets))


# def subplots(*args, **kwargs):
#     raise AssertionError("subplots なんて使うな. latex の subcaption しか勝たん.")
