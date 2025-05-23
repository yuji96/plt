# flake8: noqa
import io

import IPython.display as display
import ipywidgets
import matplotlib_fontja
import matplotlib.figure
import matplotlib.pyplot as plt
from matplotlib import cbook
from matplotlib.pyplot import *
from seaborn import kdeplot

try:
    from torch import Tensor
except:
    pass

plt.rcParams["axes.grid"] = True
plt.rcParams["figure.dpi"] = 100
plt.rcParams["figure.facecolor"] = "white"
plt.rcParams["mathtext.fontset"] = "cm"
plt.rcParams["pdf.fonttype"] = 42
plt.rcParams["savefig.bbox"] = "tight"


def detach_tensor(func):
    def wrapper(x, copy=False):
        try:
            if isinstance(x, Tensor):
                x = x.detach()
        except:
            pass
        return func(x, copy=copy)

    return wrapper


cbook.safe_masked_invalid = detach_tensor(cbook.safe_masked_invalid)


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


def add_colorbar(pad=0.02, width=0.04, im=None, ax=None, fig=None):
    if ax is None:
        ax: plt.Axes = plt.gca()
    if im is None:
        im = ax.get_images()[0]
    if fig is None:
        fig = plt.gcf()
    box = ax.get_position()
    cax = fig.add_axes([box.x1 + pad, box.y0, width, box.height])
    plt.colorbar(im, cax=cax)


def savefig(fname, bbox_inches="tight", pad_inches=0.0, **kwargs):
    return plt.savefig(fname, bbox_inches=bbox_inches, pad_inches=pad_inches, **kwargs)


# def subplots(*args, **kwargs):
#     raise AssertionError("subplots なんて使うな. latex の subcaption しか勝たん.")
