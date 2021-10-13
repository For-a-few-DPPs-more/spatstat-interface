# spatstat-interface

[![Build](https://github.com/For-a-few-DPPs-more/spatstat-interface/actions/workflows/main.yml/badge.svg)](https://github.com/For-a-few-DPPs-more/spatstat-interface/actions/workflows/main.yml)
[![PyPi version](https://badgen.net/pypi/v/spatstat-interface/)](https://pypi.org/project/spatstat-interface/)
[![codecov](https://codecov.io/gh/For-a-few-DPPs-more/spatstat-interface/branch/main/graph/badge.svg?token=BHTI6L66P2)](https://codecov.io/gh/For-a-few-DPPs-more/spatstat-interface)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Simple Python interface with the spatial statistics [R](https://www.r-project.org/) package [`spatstat`](https://github.com/spatstat/spatstat) using [`rpy2`](https://github.com/rpy2/rpy2).

## Dependecies

- [R](https://www.r-project.org/) (programming language),
- Python dependencies are listed in the [`pyproject.toml`](./pyproject.toml) file. Note that they mostly correspond to the latest version.

  ```bash
  [tool.poetry.dependencies]
  python = "^3.8"

  matplotlib = "^3.4.2"
  numpy = "^1.20.3"
  pandas = "^1.2.4"
  rpy2 = "^3.4.5"
  ```

## Installation

You may consider using `poetry` to manage your whole project as described here <https://github.com/guilgautier/template-python-project>.

### Install the project as a dependency

- Install the latest version published on [![PyPi version](https://badgen.net/pypi/v/spatstat-interface/)](https://pypi.org/project/spatstat-interface/)

  ```bash
  # activate your virtual environment an run
  poetry add spatstat-interface
  # pip install spatstat-interface
  ```

- Install from source (this may be broken)

  ```bash
  # activate your virtual environment an run
  poetry add git+https://github.com/For-a-few-DPPs-more/spatstat-interface.git
  # pip install git+https://github.com/For-a-few-DPPs-more/spatstat-interface.git
  ```

  or

  ```bash
  git clone https://github.com/For-a-few-DPPs-more/spatstat-interface.git
  cd spatstat-interface
  # activate your virtual environment an run
  poetry install --no-dev
  # pip install .
  ```

### Install in editable mode and potentially contribute to the project

#### Using `poetry`

The package can be installed in **editable** mode along with

- main (non-optional) dependencies, see `[tool.poetry.dependencies]` in [`pyproject.toml`](./pyproject.toml)
- development dependencies, `[tool.poetry.dev-dependencies]` in [`pyproject.toml`](./pyproject.toml)

```bash
git clone https://github.com/For-a-few-DPPs-more/spatstat-interface.git
cd spatstat-interface
poetry shell  # create/activate local .venv (see poetry.toml)
poetry install
```

#### Using `pip`

For now, packages defined only by a [`pyproject.toml`](./pyproject.toml) file **can't be installed editable mode directly** using `pip`.

Alternatives

- consider installing the package [using `poetry` instead](#using-poetry)

- otherwise, for your convenience, the [`pyproject.toml`](./pyproject.toml) file was duplicated into a [`setup.cfg`](./setup.cfg) file to enable editable install using `pip`.

  1. modify the `[build-system]` section in [`pyproject.toml`](./pyproject.toml) to

      ```language
      [build-system]
      requires = ["setuptools >= 40.9.0", "wheel"]
      build-backend = "setuptools.build_meta"
      ```

  2. run `pip install -e .`

## Documentation

### Main ressources

- [`notebooks`](./notebooks) for detailed examples
- [`rpy2` documentation](https://rpy2.github.io/doc.html)
- [`spatstat` documentation](https://rdocumentation.org/search?q=spatstat)

### Notes about `spatstat`

The [`spatstat`](https://github.com/spatstat/spatstat) package has recently been split into multiple sub-packages and extensions.

Using `spatstat-interface`, sub-packages and extensions are accessible in the following way

```python
from spatstat_interface import SpatstatInterface

spatstat = SpatstatInterface(update=True)
# spatstat.core is None
# spatstat.geom is None

# load/import sub-packages or extensions
spatstat.import_package("core", "geom", update=True)
spatstat.core
spatstat.geom
```

### Notes about calling functions

#### Calling R dot functions

Instead of calling `function.subfunction` as in R replace `.` by `_` in Python.

```R
# R code pcf.ppp
spatstat.core::pcf.ppp(X)
```

```Python
# Python code pcf_ppp
my_dpp = spatstat.core.pcf_ppp(X)
```

#### Using keywords arguments

Consider using Python dictionaries to pass keyword arguments.
Below are a few examples.

- dot keywords, for example passing `var.approx` keyword won't work in Python

  ```R
  # R code
  spatstat.core::pcf.ppp(X, kernel="epanechnikov", var.approx=False)
  ```

  ```Python
  # Python code
  params = {"kernel": "epanechnikov", "var.approx": False}
  my_dpp = spatstat.core.pcf_pp(X, **params)
  ```

- reserved keywords, for example `lambda` is a reserved Python keyword

  ```R
  # R code
  spatstat.core::dppGauss(lambda=rho, alpha=alpha, d=d)
  ```

  ```Python
  # Python code
  params = {"lambda": rho, "alpha": alpha, "d": d}
  my_dpp = spatstat.core.dppGauss(**params)
  ```
