import sys
from dataclasses import dataclass

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
    t_res_C: float
    bob_m3m3: float
    muob_cP: float
    pvt_corr_set: float

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
            t_res_C=self.t_res_C,
            bob_m3m3=self.bob_m3m3,
            muob_cP=self.muob_cP,
            PVT_corr_set=self.pvt_corr_set,
        )
        return fluid
