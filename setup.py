from pathlib import Path

from setuptools import setup

setup(
    name="plt",
    version="0.0.0",
    package_dir={"": "."},
    install_requires=Path(__file__).parent.joinpath(
        "requirements.txt").read_text().splitlines(),
)
