import numpy as np
import pandas as pd
import pytest
import rpy2.robjects as robjects

from spatstat_interface.interface import SpatstatInterface
from spatstat_interface.utils import to_pandas_data_frame


@pytest.fixture
def spatstat():
    spatstat = SpatstatInterface()
    spatstat.import_package("explore", "model", "geom", update=False)
    return spatstat


def test_spatstat_ppp_to_pandas_df(spatstat):
    B = [0, 1]
    bound_r = robjects.FloatVector(B)
    window = spatstat.geom.owin(xrange=bound_r, yrange=bound_r)

    X_np = list(B[0] + (B[1] - B[0]) * np.random.rand(100))
    X = robjects.FloatVector(X_np)
    points_ppp = spatstat.geom.ppp(X, X, window=window)
    pcf_ppp = spatstat.explore.pcf_ppp(points_ppp)

    pcf_pd = to_pandas_data_frame(pcf_ppp)
    assert isinstance(pcf_pd, pd.DataFrame)


def test_simulate_dpp_gaussian(spatstat):
    params = {"lambda": 100, "alpha": 0.05, "d": 2}
    my_dpp = spatstat.model.dppGauss(**params)
    bound = robjects.FloatVector([0, 1])
    window = spatstat.geom.owin(xrange=bound, yrange=bound)

    spatstat.model.simulate_dppm(my_dpp, W=window)
    assert True
