from typing import Any

import numpy as np
import python_api as unifloc

from core.base import BaseCore
from data.config_data import Data
from data.pvt_data import PVTData


class UniflocCore(BaseCore):
    controler: unifloc.API = unifloc.API(
        "Unifloc_VBA7.xlam"
    )  # Нужно найти правильный путь

    def __init__(self, dataset: Data, pvt_data: PVTData):
        self.dataset = dataset
        self.pvt_data = pvt_data
        self.pvt = self.generate_encode_pvt()

    def generate_encode_pvt(self) -> Any:
        return self.controler.encode_PVT(**self.dataset)

    def calculate_rs(self) -> np.ndarray:
        rs = self.controler.PVT_rs_m3m3(PVT_json=self.pvt, **self.pvt_data)
        return rs
