import sys
from dataclasses import dataclass
from typing import List, Tuple

from ufpy.pvt import PVT

unifloc_path = r"C:\unifloc_vba-master"
unifloc_vba = unifloc_path + r"\UniflocVBA_7.xlam"
sys.path.insert(0, unifloc_path)
import unifloc_vba_python_api.python_api as unifloc


@dataclass
class DefaultConfig:
    gamma_gas: float
    gamma_oil: float
    gamma_wat: float
    rsb_m3m3: float
    pb_atma: float
    t_res_c: float
    bob_m3m3: float
    muob_cp: float
    pvt_corr_set: float

    def initiate_pvt(self) -> PVT:
        pvt = PVT()
        pvt.init(
            gamma_gas=self.gamma_gas,
            gamma_oil=self.gamma_oil,
            gamma_wat=self.gamma_wat,
            rsb_m3m3=self.rsb_m3m3,
            pb_atma=self.pb_atma,
            bob_m3m3=self.bob_m3m3,
            muob_cP=self.muob_cp,
            t_res_C=self.t_res_c,
        )
        return pvt

    @staticmethod
    def initiate_unifloc_api():
        unf = unifloc.API(unifloc_vba)
        return unf

    def initiate_unifloc(self):
        fluid = self.initiate_unifloc_api().encode_PVT(
            gamma_gas=self.gamma_gas,
            gamma_oil=self.gamma_oil,
            gamma_wat=self.gamma_wat,
            rsb_m3m3=self.rsb_m3m3,
            pb_atma=self.pb_atma,
            t_res_C=self.t_res_c,
            bob_m3m3=self.bob_m3m3,
            muob_cP=self.muob_cp,
            PVT_corr_set=self.pvt_corr_set,
        )
        return fluid


class Config:
    def __init__(
        self, name: str, data_fluid: DefaultConfig, data_for_test: List[Tuple]
    ):
        self._name = name
        self.tested_data: List[Tuple] = data_for_test
        self.fluid_as_ufpy: PVT = data_fluid.initiate_pvt()
        self.unifloc_api = data_fluid.initiate_unifloc_api()
        self.fluid_as_unifloc = data_fluid.initiate_unifloc()
