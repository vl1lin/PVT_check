import numpy as np
import pytest

from core.compare_core import CompareCore
from data.pvt_data import PVTData
from tests.conftest import PVT_Test_data_pb, PVT_Test_data_rs_bo


@pytest.mark.parametrize("p_atma, t_C", PVT_Test_data_rs_bo)
def test_compare_core_rs_bo(base_pvt, p_atma, t_C):
    testing_data = PVTData(p_atma, t_C)
    compare_core = CompareCore(base_pvt, testing_data)
    rs_diff = compare_core.compare_rs()
    bo_diff = compare_core.compare_bo()
    assert np.all(rs_diff <= 5)
    assert np.all(bo_diff <= 5)


@pytest.mark.parametrize("t_C, rsb_m3m3", PVT_Test_data_pb)
def test_compare_core_pb(base_pvt, t_C, rsb_m3m3):
    testing_data = PVTData(None, t_C, rsb_m3m3)
    compare_core = CompareCore(base_pvt, testing_data)
    pb_diff = compare_core.compare_pb()
    assert np.all(pb_diff <= 5)
