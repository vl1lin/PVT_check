from typing import Type

import numpy as np

from core.unfpy_core import UnfpyCore
from core.unifloc_core import UniflocCore
from data.config_data import Data
from data.pvt_data import PVTData


class CompareCore:
    _unfpy: Type[UnfpyCore] = UnfpyCore
    _unifloc: Type[UniflocCore] = UniflocCore

    def __init__(self, dataset: Data, pvt_data: PVTData):
        self.dataset = dataset
        self.pvt_data = pvt_data
        self.unfpy = self._unfpy(dataset, pvt_data)
        self.unifloc = self._unifloc(dataset, pvt_data)

    def compare_rs(self) -> np.ndarray:
        """
        Сравнение значений Rs между Unfpy и Unifloc
        :return: Массив относительных погрешностей
        """
        rs_unfpy = self.unfpy.calculate_rs()
        rs_unifloc = self.unifloc.calculate_rs()
        return np.abs(rs_unfpy - rs_unifloc) / rs_unfpy * 100

    def compare_bo(self) -> np.ndarray:
        """
        Сравнение значений Bo между Unfpy и Unifloc
        :return: Массив относительных погрешностей
        """
        bo_unfpy = self.unfpy.calculate_bo()
        bo_unifloc = self.unifloc.calculate_bo()
        return np.abs(bo_unfpy - bo_unifloc) / bo_unfpy * 100

    def compare_pb(self) -> np.ndarray:
        """
        Сравнение значений Pb между Unfpy и Unifloc
        :return: Массив относительных погрешностей
        """
        pb_unfpy = self.unfpy.calculate_pb()
        pb_unifloc = self.unifloc.calculate_pb()
        return np.abs(pb_unfpy - pb_unifloc) / pb_unfpy * 100
