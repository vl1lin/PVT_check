from typing import Any

import numpy as np
import python_api as unifloc

from core.base import BaseCore
from data.config_data import Data
from data.pvt_data import PVTData


class UniflocCore(BaseCore):
    controler: unifloc.API = unifloc.API(
        r"C:\unifloc_vba-master" + r"\UniflocVBA_7.xlam"
    )  # Нужно найти правильный путь

    def __init__(self, dataset: Data, pvt_data: PVTData):
        self.dataset = dataset
        self.pvt_data = pvt_data
        self.pvt = self.generate_encode_pvt()

    def generate_encode_pvt(self) -> Any:
        return self.controler.encode_PVT(**self.dataset)

    def calculate_rs(self) -> np.ndarray:
        rs = np.array(
            [
                self.controler.PVT_rs_m3m3(PVT_json=self.pvt, p_atma=i, t_C=j)
                for i, j in zip(self.pvt_data.p_atma, self.pvt_data.t_C)
            ]
        )
        return rs

    def calculate_pb(self) -> np.ndarray:
        pb = np.array(
            [
                self.controler.PVT_pb_atma(
                    PVT_json=self.controler.encode_PVT(rsb_m3m3=rsb, **self.dataset),
                    t_C=t,
                )
                for t, rsb in zip(self.pvt_data.t_C, self.pvt_data.rsb_m3m3)
            ]
        )
        return pb

    def calculate_bo(self) -> np.ndarray:
        bo = np.array(
            [
                self.controler.PVT_bo_m3m3(PVT_json=self.pvt, p_atma=i, t_C=j)
                for i, j in zip(self.pvt_data.p_atma, self.pvt_data.t_C)
            ]
        )
        return bo
