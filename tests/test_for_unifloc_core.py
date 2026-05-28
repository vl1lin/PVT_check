import numpy as np
import pytest

from core.unifloc_core import UniflocCore
from data.pvt_data import PVTData
from tests.conftest import PVT_Test_data_pb, PVT_Test_data_rs_bo


@pytest.mark.parametrize("p_atma, t_c", PVT_Test_data_rs_bo)
def test_unifloc_core_bo_rs(base_pvt, p_atma, t_c):
    testing_data = PVTData(p_atma, t_c)
    core = UniflocCore(base_pvt, testing_data)
    assert np.all(core.calculate_rs() > 0)
    assert np.all(core.calculate_bo() > 1)


@pytest.mark.parametrize("t_c, rsb_m3m3", PVT_Test_data_pb)
def test_unifloc_core_pb(base_pvt, t_c, rsb_m3m3):
    testing_data = PVTData(None, t_c, rsb_m3m3)
    core = UniflocCore(base_pvt, testing_data)
    assert np.all(core.calculate_pb() > 0)
