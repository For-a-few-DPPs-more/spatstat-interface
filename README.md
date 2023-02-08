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
      - [Editable install with `poetry`](#editable-install-with-poetry)
      - [Editable install with `pip`](#editable-install-with-pip)
  - [Documentation](#documentation)
    - [Main resources](#main-resources)
    - [Notes about `spatstat`](#notes-about-spatstat)
    - [Calling functions](#calling-functions)
      - [Calling function.variant](#calling-functionvariant)
      - [Keyword arguments](#keyword-arguments)

Simple Python interface with the spatial statistics [R](https://www.r-project.org/) package [`spatstat`](https://github.com/spatstat/spatstat) using [`rpy2`](https://github.com/rpy2/rpy2).

## Dependencies

- [R](https://www.r-project.org/) (programming language)
  - [`spatstat`](https://github.com/spatstat/spatstat) package, which [has recently been split into multiple sub-packages and extensions](https://github.com/spatstat/spatstat#spatstat-has-been-split-into-a-family-of-packages). **Warning: potential new splits may break your code!**
- Python >= 3.7, with dependencies listed in the [`pyproject.toml`](./pyproject.toml) file. Note that they mostly correspond to the latest version.
  - non-optional dependencies are [`pandas`](https://pandas.pydata.org/) and [`rpy2`](https://rpy2.github.io/).

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

#### Editable install with `poetry`

The package can be installed in **editable** mode along with

- main (non-optional) dependencies, see `[tool.poetry.dependencies]` in [`pyproject.toml`](./pyproject.toml)
- development dependencies, `[tool.poetry.group.dev.dependencies]` in [`pyproject.toml`](./pyproject.toml)

```bash
cd spatstat-interface
# poetry shell  # to create/activate local .venv (see poetry.toml)
poetry install
# poetry install --with dev
# poetry install --with dev --extras "notebook"
```

#### Editable install with `pip`

Consider using [`pip>=21.3.1`](https://pip.pypa.io/en/stable/news/#v21-3-1), when installing packages defined by a `pyproject.toml` file.

```bash
cd spatstat-interface
# activate your virtual environment and run
pip install --editable .
# pip install --editable ".[notebook]" to install notebook dependencies
```

See also the [`pip install`](https://pip.pypa.io/en/stable/cli/pip_install/) optional commands.

## Documentation

### Main resources

- [`notebooks`](./notebooks) showcase detailed examples
- [`rpy2` documentation](https://rpy2.github.io/doc.html)
- [`spatstat` documentation](https://rdocumentation.org/search?q=spatstat)

### Notes about `spatstat`

The [`spatstat`](https://github.com/spatstat/spatstat) package [has recently been split into multiple sub-packages and extensions](https://github.com/spatstat/spatstat#spatstat-has-been-split-into-a-family-of-packages).
**Warning: potential new splits may break your code!**

Using `spatstat-interface`, sub-packages and extensions are accessible in the following way

```python
from spatstat_interface.interface import SpatstatInterface

spatstat = SpatstatInterface()
# spatstat.spatstat is None
# spatstat.model is None
# spatstat.explore is None
# spatstat.geom is None

# load/import sub-packages or extensions
spatstat.import_package("model", "explore", "geom", update=True)
spatstat.model
spatstat.explore
spatstat.geom
```

### Calling functions

#### Calling function.variant

To call the R `function.variant`

```R
# R code pcf.ppp
spatstat.explore::pcf.ppp(X)
```

Replace `.` by `_` to call `function_variant` in Python

```Python
# Python code pcf_ppp
spatstat.explore.pcf_ppp(X)
```

#### Keyword arguments

Consider using Python dictionaries to pass keyword arguments.
Below are a few examples.

- dot keywords, for example passing `var.approx` keyword argument won't work in Python

  ```R
  # R code
  spatstat.explore::pcf.ppp(X, kernel="epanechnikov", var.approx=False)
  ```

  ```Python
  # Python code
  params = {"kernel": "epanechnikov", "var.approx": False}
  spatstat.explore.pcf_ppp(X, **params)
  ```

- reserved keywords, for example `lambda` is a reserved Python keyword; it can't be used as a keyword argument

  ```R
  # R code
  spatstat.model::dppGauss(lambda=rho, alpha=alpha, d=d)
  ```

  ```Python
  # Python code
  params = {"lambda": rho, "alpha": alpha, "d": d}
  spatstat.model.dppGauss(**params)
  ```
