# Notebooks

## Run a notebook remotely

- `spatstat_playground.ipynb` [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/For-a-few-DPPs-more/spatstat-interface/blob/main/notebooks/spatstat_playground.ipynb)

## Run a notebook locally

1. It is suggested you clone the repository to get the latest version of the source code

    ```bash
    git clone https://github.com/For-a-few-DPPs-more/spatstat-interface.git
    cd spatstat-interface
    git pull origin main
    ```

2. Then, install the project in a virtual environment, see also the [installation instructions on GitHub](https://github.com/For-a-few-DPPs-more/spatstat-interface/blob/main/README.md#Installation)

    - if you use [`poetry`](https://python-poetry.org/)

        ```bash
        # cd spatstat-interface
        poetry shell  # to create/activate local .venv (see poetry.toml)
        poetry install -E notebook  # (see [tool.poetry.extras] in pyproject.toml)
        ```

    - if you use [`pip`](https://pip.pypa.io/en/stable/)

        ```bash
        # cd spatstat-interface
        # activate a virtual environment of your choice and run
        pip install '.[notebook]'  # (see [tool.poetry.extras] in pyproject.toml)
        ```

3. Finally, launch the notebook

    - with your favorite notebook interface, VSCode for example
    - or if you use [`poetry`](https://python-poetry.org/), run

        ```bash
        # cd spatstat-interface
        poetry run jupyter notebook
        ```

    - or if you don't use poetry, run

        ```bash
        # cd spatstat-interface
        jupyter notebook
        ```
