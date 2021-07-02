# spatstat-interface

[![Build](https://github.com/For-a-few-DPPs-more/spatstat-interface/actions/workflows/main.yml/badge.svg)](https://github.com/For-a-few-DPPs-more/spatstat-interface/actions/workflows/main.yml)
[![codecov](https://codecov.io/gh/For-a-few-DPPs-more/spatstat-interface/branch/main/graph/badge.svg?token=BHTI6L66P2)](https://codecov.io/gh/For-a-few-DPPs-more/spatstat-interface)

Simple Python interface with the spatial statistics R package [spatstat](https://github.com/spatstat/spatstat) using [rpy2](https://github.com/rpy2/rpy2)

## Installation

### Requirements

* [R](https://www.r-project.org/) (programming language)
* see python dependencies in [pyproject.toml](./pyproject.toml)

Once packaged and pushed on [PyPI](https://pypi.org/)

```bash
pip install spatstat-interface
```

## Documentation

* [notebooks](./notebooks) for detailed examples
* [rpy2 documentation](https://rpy2.github.io/doc.html)
* [spatstat documentation](https://rdocumentation.org/search?q=spatstat)

The [spatstat](https://github.com/spatstat/spatstat) package has recently been split into multiple subpackages and extensions.
Access to subpackages or extensions in the following way

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
