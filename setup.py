from pathlib import Path

from setuptools import setup

setup(
    name="plt",
    version="0.2.0",
    py_modules=["plt"],
    install_requires=Path(__file__)
    .parent.joinpath("requirements.txt")
    .read_text()
    .splitlines(),
)
