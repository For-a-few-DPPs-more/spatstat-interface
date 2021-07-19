# spatstat-interface

[![Build](https://github.com/For-a-few-DPPs-more/spatstat-interface/actions/workflows/main.yml/badge.svg)](https://github.com/For-a-few-DPPs-more/spatstat-interface/actions/workflows/main.yml)
[![codecov](https://codecov.io/gh/For-a-few-DPPs-more/spatstat-interface/branch/main/graph/badge.svg?token=BHTI6L66P2)](https://codecov.io/gh/For-a-few-DPPs-more/spatstat-interface)

Simple Python interface with the spatial statistics R package [spatstat](https://github.com/spatstat/spatstat) using [rpy2](https://github.com/rpy2/rpy2).

## Dependecies

* [R](https://www.r-project.org/) (programming language), 
* Python dependencies are listed in the [pyproject.toml](https://github.com/For-a-few-DPPs-more/spatstat-interface/blob/main/pyproject.toml) file.

## Installation

1) To install the lastest test version from [TestPyPi](https://test.pypi.org/project/spatstat-interface/)

```bash
pip install -i https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ spatstat-interface
```

2) To install the latest development version from [GitHub](https://github.com/For-a-few-DPPs-more/spatstat-interface)

```bash
git clone https://github.com/For-a-few-DPPs-more/spatstat-interface.git
cd spatstat-interface
pip install .
```

3) To install the latest stable version **once the package will be available on on [PyPI](https://pypi.org/)**

```bash
pip install spatstat-interface
```

## Documentation

* [notebooks](https://github.com/For-a-few-DPPs-more/spatstat-interface/blob/main/notebooks) for detailed examples
* [rpy2 documentation](https://rpy2.github.io/doc.html)
* [spatstat documentation](https://rdocumentation.org/search?q=spatstat)

The [spatstat](https://github.com/spatstat/spatstat) package has recently been split into multiple subpackages and extensions.

Using `spatstat-interface` , subpackages and extensions are accessible in the following way

```python
from spatstat_interface import SpatstatInterface
spatstat = SpatstatInterface(update=True)
# spatstat.core is None
# spatstat.geom is None

# load/import subpackages or extensions
spatstat.import_package("core", "geom", update=False)
spatstat.core
spatstat.geom
```
