# spatstat-interface

[![Build](https://github.com/For-a-few-DPPs-more/spatstat-interface/actions/workflows/main.yml/badge.svg)](https://github.com/For-a-few-DPPs-more/spatstat-interface/actions/workflows/main.yml)
[![PyPi version](https://badgen.net/pypi/v/spatstat-interface/)](https://pypi.org/project/spatstat-interface/)
[![codecov](https://codecov.io/gh/For-a-few-DPPs-more/spatstat-interface/branch/main/graph/badge.svg?token=BHTI6L66P2)](https://codecov.io/gh/For-a-few-DPPs-more/spatstat-interface)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

- [spatstat-interface](#spatstat-interface)
  - [Dependencies](#dependencies)
  - [Installation](#installation)
    - [Install the project as a dependency](#install-the-project-as-a-dependency)
    - [Install in editable mode and potentially contribute to the project](#install-in-editable-mode-and-potentially-contribute-to-the-project)
      - [Using `poetry`](#using-poetry)
      - [Using `pip`](#using-pip)
  - [Documentation](#documentation)
    - [Main ressources](#main-ressources)
    - [Notes about `spatstat`](#notes-about-spatstat)
    - [Notes about calling functions](#notes-about-calling-functions)
      - [Calling function.variant](#calling-functionvariant)
      - [Using keyword arguments](#using-keyword-arguments)

Simple Python interface with the spatial statistics [R](https://www.r-project.org/) package [`spatstat`](https://github.com/spatstat/spatstat) using [`rpy2`](https://github.com/rpy2/rpy2).

## Dependencies

- [R](https://www.r-project.org/) (programming language),
- Python dependencies are listed in the [`pyproject.toml`](./pyproject.toml) file. Note that they mostly correspond to the latest version.

  ```toml
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

### Install in editable mode and potentially contribute to the project

You may consider [forking the repository](https://github.com/For-a-few-DPPs-more/spatstat-interface/fork).

In any case, your can clone the repository

- if you have forked the repository

  ```bash
  git clone https://github.com/your_user_name/spatstat-interface.git
  ```

- if you have **not** forked the repository

  ```bash
  git clone https://github.com/For-a-few-DPPs-more/spatstat-interface.git
  ```

#### Using `poetry`

The package can be installed in **editable** mode along with

- main (non-optional) dependencies, see `[tool.poetry.dependencies]` in [`pyproject.toml`](./pyproject.toml)
- development dependencies, `[tool.poetry.dev-dependencies]` in [`pyproject.toml`](./pyproject.toml)

```bash
cd spatstat-interface
# activate your virtual environment or run
# poetry shell  # to create/activate local .venv (see poetry.toml)
poetry install
# poetry install --no-dev  # to avoid installing the development dependencies
```

#### Using `pip`

For now, packages defined only by a [`pyproject.toml`](./pyproject.toml) file **can't be installed editable mode directly** using `pip`.

Alternatives

1. consider [using `poetry` instead](#using-poetry)

2. otherwise, for your convenience, the [`pyproject.toml`](./pyproject.toml) file was duplicated into a [`setup.cfg`](./setup.cfg) file to enable editable install using `pip`.

   - modify the `[build-system]` section in [`pyproject.toml`](./pyproject.toml) to

      ```toml
      [build-system]
      requires = ["setuptools >= 40.9.0", "wheel"]
      build-backend = "setuptools.build_meta"
      ```

   - intstall the project in editable mode

      ```bash
      cd spatstat-interface
      # activate your virtual environment and run
      pip install -e .
      ```

## Documentation

### Main ressources

- [`notebooks`](./notebooks) showcase detailed examples
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

#### Calling function.variant

Instead of calling `function.variant` as in R replace `.` by `_` in Python.

```R
# R code pcf.ppp
spatstat.core::pcf.ppp(X)
```

```Python
# Python code pcf_ppp
my_dpp = spatstat.core.pcf_ppp(X)
```

#### Using keyword arguments

Consider using Python dictionaries to pass keyword arguments.
Below are a few examples.

- dot keywords, for example passing `var.approx` keyword argument won't work in Python

  ```R
  # R code
  spatstat.core::pcf.ppp(X, kernel="epanechnikov", var.approx=False)
  ```

  ```Python
  # Python code
  params = {"kernel": "epanechnikov", "var.approx": False}
  my_dpp = spatstat.core.pcf_pp(X, **params)
  ```

- reserved keywords, for example `lambda` is a reserved Python keyword ; it can't be used as a keyword argument

  ```R
  # R code
  spatstat.core::dppGauss(lambda=rho, alpha=alpha, d=d)
  ```

  ```Python
  # Python code
  params = {"lambda": rho, "alpha": alpha, "d": d}
  my_dpp = spatstat.core.dppGauss(**params)
  ```
