# import importlib.resources
import os
import setuptools

NAME = "ebisim"
EMAIL = None
DESCRIPTION = "A package for simulating the charge state distribution evolution in an EBIS/EBIT."
URL = "https://github.com/HPLegion/ebisim"
PYTHON_REQUIRES = ">=3.7.0"
INSTALL_REQUIRES = ["numpy", "scipy", "pandas", "numba", "matplotlib"]
CLASSIFIERS = ["Programming Language :: Python :: 3.7"]

with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()

def from_init(attr):
    # text = importlib.resources.read_text("ebisim", "__init__.py")
    loc = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(loc, "ebisim", "__init__.py")) as f:
        text = f.read()
    for line in text.split("\n"):
        if line.strip().startswith(attr):
            return line.split("=")[-1].strip(" \n\'\"")
    return "attr not found"


VERSION = from_init("__init__")
AUTHOR = from_init("__author__")

setuptools.setup(
    name=NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=EMAIL,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url=URL,
    python_requires=PYTHON_REQUIRES,
    install_requires=INSTALL_REQUIRES,
    packages=setuptools.find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
    include_package_data=True,
    classifiers=CLASSIFIERS,
)
