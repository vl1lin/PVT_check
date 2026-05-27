import numpy as np
import pytest

from core.unfpy_core import UnfpyCore
from data.config_data import Data
from data.pvt_data import PVTData


@pytest.fixture
def base_pvt():
    data = Data(
        gamma_oil=0.8,
        gamma_wat=0.6,
        gamma_gas=0.4,
        pvt_corr=0,
    )
    return data


@pytest.mark.parametrize(
    "p_atma, t_c",
    [
        (np.array([100, 200, 300, 400]), np.array([20, 30, 40, 50])),
        (np.array([200, 300, 400, 500]), np.array([30, 40, 50, 60])),
        (np.array([300, 400, 500, 600]), np.array([40, 50, 60, 70])),
        (np.array([400, 500, 600, 700]), np.array([50, 60, 70, 80])),
    ],
)
def test_of_unfpy_core(base_pvt, p_atma, t_c):
    testing_data = PVTData(p_atma, t_c)
    core = UnfpyCore(base_pvt, testing_data)
    assert np.all(core.calculate_rs() > 0)
    # assert np.all(core.calculate_pb() > 0)
    assert np.all(core.calculate_bo() > 1)
