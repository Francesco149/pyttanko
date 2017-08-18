try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import pyttanko

pyttanko_classifiers = [
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 3",
    "Intended Audience :: Developers",
    "License :: Public Domain",
    "Topic :: Software Development :: Libraries",
    "Topic :: Utilities",
]

with open("README.rst", "r") as f:
    pyttanko_readme = f.read()

setup(
    name="pyttanko",
    version=pyttanko.__version__,
    author="Franc[e]sco",
    author_email="lolisamurai@tfwno.gf",
    url="https://github.com/Francesco149/pyttanko",
    py_modules=["pyttanko"],
    description="osu! pp and difficulty calculator",
    long_description=pyttanko_readme,
    license="Unlicense",
    classifiers=pyttanko_classifiers,
    keywords="osu! osu"
)
