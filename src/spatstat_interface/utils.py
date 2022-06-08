import rpy2.robjects as robjects
import rpy2.robjects.packages as rpackages
from rpy2.robjects import pandas2ri
from rpy2.robjects.conversion import localconverter


def install_r_package(*names, update=False):
    """Install ``R`` package(s) passed via ``names``, using `rpy2.robjects.packages.importr <https://rpy2.github.io/doc/latest/html/robjects_rpackages.html?highlight=importr#rpy2.robjects.packages.importr>`_.

    If the corresponding package is already installed it is updated (latest version) according to ``update``, otherwise it is installed (latest version).

    .. code-block:: python

        install_r_package("spatstat.core", "spatstat.geom", update=False)
    """
    utils = rpackages.importr("utils")
    for name in names:
        if rpackages.isinstalled(name) and not update:
            continue
        # Choose mirror (internet access required) if update = True
        utils.chooseCRANmirror(ind=1)
        utils.install_packages(name)


def to_pandas_data_frame(r_data_frame):
    """Convert the R DataFrame ``r_data_frame`` object to a ``pandas.DataFrame`` object `using rpy2 <https://rpy2.github.io/doc/latest/html/pandas.html>`_."""
    with localconverter(robjects.default_converter + pandas2ri.converter):
        pandas_df = robjects.conversion.rpy2py(r_data_frame)
        return pandas_df
