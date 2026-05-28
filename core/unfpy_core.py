import numpy as np
import unfpy.api as unf

from core.base import BaseCore
from data.config_data import Data
from data.pvt_data import PVTData


class UnfpyCore(BaseCore):
    def __init__(self, dataset: Data, training_data: PVTData):
        self.dataset: Data = dataset
        self.pvt_data: PVTData = training_data

    def calculate_rs(
        self,
    ) -> np.ndarray:
        rs = unf.pvt_rs_m3m3(
            gamma_oil=self.dataset["gamma_oil"],
            gamma_gas=self.dataset["gamma_gas"],
            **self.pvt_data,
        )
        return rs

    def calculate_pb(self) -> np.ndarray:
        pb = unf.pvt_pb_atma(
            self.pvt_data.t_c,
            gamma_oil=self.dataset["gamma_oil"],
            gamma_gas=self.dataset["gamma_gas"],
        )
        return pb

    def calculate_bo(self) -> np.ndarray:
        bo = unf.pvt_b_oil_m3m3(
            gamma_oil=self.dataset["gamma_oil"],
            gamma_gas=self.dataset["gamma_gas"],
            **self.pvt_data,
        )
        return bo
