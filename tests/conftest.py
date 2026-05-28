import matplotlib
import numpy as np
import pytest

matplotlib.use("Agg")

from core.compare_core import CompareCore
from data.config_data import Data
from data.pvt_data import PVTData


@pytest.fixture
def base_pvt():
    data = Data(
        gamma_oil=0.8,
        gamma_wat=1,
        gamma_gas=0.4,
        PVT_corr_set=0,
    )
    return data


@pytest.fixture
def pvt_data_rs_bo():
    return PVTData(
        np.array([100, 200, 300]),
        np.array([20, 30, 40]),
    )


@pytest.fixture
def pvt_data_pb():
    return PVTData(
        None,
        np.array([20, 30, 40]),
        np.array([50, 100, 150]),
    )


@pytest.fixture
def compare_core_rs_bo(base_pvt, pvt_data_rs_bo):
    return CompareCore(base_pvt, pvt_data_rs_bo)


@pytest.fixture
def compare_core_pb(base_pvt, pvt_data_pb):
    return CompareCore(base_pvt, pvt_data_pb)


PVT_Test_data_rs_bo = [
    (np.array([100, 200, 300, 400]), np.array([20, 30, 40, 50])),
    (np.array([200, 300, 400, 500]), np.array([30, 40, 50, 60])),
    (np.array([300, 400, 500, 600]), np.array([40, 50, 60, 70])),
    (np.array([400, 500, 600, 700]), np.array([50, 60, 70, 80])),
]

PVT_Test_data_pb = [
    (np.array([20, 30, 40, 50]), np.array([20, 30, 40, 50])),
    (np.array([70, 80, 90, 100]), np.array([70, 80, 90, 100])),
    (np.array([110, 120, 130, 140]), np.array([110, 120, 130, 140])),
    (np.array([91, 92, 93, 94, 95]), np.array([150, 160, 165, 166, 167])),
]
