# flake8: noqa
import io

import IPython.display as display
import ipywidgets
import matplotlib_fontja
from matplotlib.figure import Figure
from matplotlib_inline.backend_inline import set_matplotlib_formats
import matplotlib.pyplot as plt
from matplotlib import cbook
from matplotlib.pyplot import *
from seaborn import kdeplot

try:
    from torch import Tensor
except:
    pass

plt.rcParams["axes.grid"] = True
# plt.rcParams["figure.dpi"] = 100
plt.rcParams["figure.facecolor"] = "white"
plt.rcParams["mathtext.fontset"] = "cm"
plt.rcParams["savefig.bbox"] = "tight"
plt.rcParams["pdf.fonttype"] = 42
plt.rcParams["font.size"] = 10

# set_matplotlib_formats("svg")


def detach_tensor(func):
    def wrapper(x):
        try:
            if isinstance(x, Tensor):
                x = x.detach().cpu()
        except:
            pass
        return func(x)

    return wrapper


cbook._unpack_to_numpy = detach_tensor(cbook._unpack_to_numpy)


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


def figure(
    # autoincrement if None, else integer from 1-N
    num=None,
    # defaults to rc figure.figsize
    figsize=None,
    # defaults to rc figure.dpi
    dpi: float | None = None,
    *,
    # defaults to rc figure.facecolor
    facecolor=None,
    # defaults to rc figure.edgecolor
    edgecolor=None,
    frameon: bool = True,
    FigureClass: type[Figure] = Figure,
    clear: bool = False,
    cm=True,
    w=10,
    h=4,
    scale=1.0,
    **kwargs,
):
    if cm:
        w = w / 2.54  # cm to inch
        h = h / 2.54  # cm to inch
    figsize = (w, h) if figsize is None else figsize
    figsize = tuple([scale * x for x in figsize])

    return plt.figure(
        num,
        figsize,
        dpi,
        facecolor=facecolor,
        edgecolor=edgecolor,
        frameon=frameon,
        FigureClass=FigureClass,
        clear=clear,
        **kwargs,
    )


# def subplots(*args, **kwargs):
#     raise AssertionError("subplots なんて使うな. latex の subcaption しか勝たん.")
