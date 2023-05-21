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


def hbox(figures: list[matplotlib.figure.Figure], **kwargs):
    kwargs.setdefault("width", 400)
    widgets = []
    for fig in figures:
        buf = io.BytesIO()
        fig.savefig(buf, format="png")
        widgets.append(ipywidgets.Image(value=buf.getvalue(), format="png", **kwargs))
    display.display(ipywidgets.HBox(widgets))
