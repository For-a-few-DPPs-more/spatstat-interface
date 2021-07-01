import rpy2.robjects as robjects
import rpy2.robjects.packages as rpackages
from rpy2.robjects import pandas2ri
from rpy2.robjects.conversion import localconverter


def install_r_package(*names, update=True):
    """Install ``R`` package(s) passed via ``names``.
    If the corresponding package(s) is already installed it is updated (latest version) according to ``update``, otherwise it installed (latest version).

    .. code-block:: python

        install_r_package("spatstat", ..., update=True)

    :param update: trigger installation of the latest version of the package, defaults to True
    :type update: bool, optional
    """
    # todo: pass version argument
    # ? seems that it is not possible using utils, maybe try with
    utils = rpackages.importr("utils")
    for name in names:
        if rpackages.isinstalled(name) and not update:
            continue
        # Choose mirror (internet access required) if update = True
        utils.chooseCRANmirror(ind=1)
        utils.install_packages(name)


def convert_r_df_to_pandas_df(r_df):
    """`Convert R DataFrame to pandas DataFrame using rpy2 <https://rpy2.github.io/doc/latest/html/pandas.html>`_

    :param r_df: R DataFrame
    :return: pandas DataFrame created from ``r_df``
    """
    with localconverter(robjects.default_converter + pandas2ri.converter):
        pandas_df = robjects.conversion.rpy2py(r_df)
        return pandas_df
