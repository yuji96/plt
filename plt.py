# flake8: noqa
import io

import IPython.display as display
import ipywidgets
import japanize_matplotlib
import matplotlib.figure
import matplotlib.pyplot as plt
from matplotlib.pyplot import *
from seaborn import kdeplot

plt.rcParams["axes.grid"] = True
plt.rcParams["figure.dpi"] = 100
plt.rcParams["figure.facecolor"] = "white"
plt.rcParams["mathtext.fontset"] = "cm"
plt.rcParams["pdf.fonttype"] = 42
plt.rcParams["savefig.bbox"] = "tight"


def imshow(*args, **kwargs):
    im = plt.imshow(*args, **kwargs)
    plt.gca().grid(False)
    return im


def hbox(*iterable, **kwargs):
    kwargs.setdefault("width", 400)

    figures = []
    for x in zip(*iterable):
        if len(iterable) == 1:
            yield x[0]
        else:
            yield x
        figures.append(plt.gcf())
        plt.close()

    widgets = []
    for fig in figures:
        buf = io.BytesIO()
        fig.savefig(buf, format="png")
        widgets.append(ipywidgets.Image(value=buf.getvalue(), format="png", **kwargs))
    display.display(ipywidgets.HBox(widgets))


# def subplots(*args, **kwargs):
#     raise AssertionError("subplots なんて使うな. latex の subcaption しか勝たん.")
