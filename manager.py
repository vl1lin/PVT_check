"""В данном файле содержится класс менеджер для управления объектами"""

from collections.abc import Iterable
from typing import Optional

import numpy as np

from configs.default import DefaultConfig
import python_api as unifloc
import unfpy as unf

class Manager:
    def __init__(self):
        self._data: Optional[DefaultConfig] = None
        self._p_atma: np.ndarray | float
        self._t_c: np.ndarray | float
        self.pvt = unf.PVT()
        self._rs_m3m3: np.ndarray
        self._bo_m3m3: np.ndarray
        self._pb_atma: np.ndarray

    @property
    def dataset(self) -> Optional[DefaultConfig]:
        """Возвращает текущий датасет"""
        return self._data

    @dataset.setter
    def dataset(self, value: Optional[DefaultConfig]):
        """Устанавливает текущий датасет"""
        self._data = value

    @property
    def p_atma(self) -> np.ndarray | float:
        """Возвращает массив давления в атмосферах"""
        return self._p_atma

    @p_atma.setter
    def p_atma(self, value: Iterable[float] | float):
        """
        Устанавливает массив давления в атмосферах
        :param value: Итерируемый объект, содержащий значения давления в атмосферах
        """
        if not isinstance(value, Iterable):
            self._p_atma = value
        else:
            self._p_atma = np.array(value)

    @property
    def t_c(self) -> np.ndarray | float:
        """Возвращает массив температуры в градусах Цельсия"""
        return self._t_c

    @t_c.setter
    def t_c(self, value: Iterable[float] | float):
        """
        Устанавливает массив температуры в градусах Цельсия
        :param value: Итерируемый объект, содержащий значения температуры в градусах Цельсия
        """
        if not isinstance(value, Iterable):
            self._t_c = value
        else:
            self._t_c = np.array(value)

    @property
    def rs_m3m3(self) -> np.ndarray:
        """Возвращает массив rs_m3m3"""
        return self._rs_m3m3

    @rs_m3m3.setter
    def rs_m3m3(
        self,
        p_atma: np.ndarray | float,
        t_c: np.ndarray | float,
    ):
        """
        Устанавливает массив rs_m3m3
        :param value: Итерируемый объект, содержащий значения rs_m3m3
        """
        if isinstance(p_atma, Iterable) or isinstance(t_c, Iterable):
            self._rs_m3m3 =
        else:
            self._rs_m3m3 = np.array(value)

    @property
    def bo_m3m3(self) -> np.ndarray:
        """Возвращает массив bo_m3m3"""
        return self._bo_m3m3

    @bo_m3m3.setter
    def bo_m3m3(self, value: Iterable[float] | float):
        """
        Устанавливает массив bo_m3m3
        :param value: Итерируемый объект, содержащий значения bo_m3m3
        """
        if not isinstance(value, Iterable):
            self._bo_m3m3 = value
        else:
            self._bo_m3m3 = np.array(value)

    @property
    def pb_atma(self) -> np.ndarray:
        """Возвращает массив pb_atma"""
        return self._pb_atma

    @pb_atma.setter
    def pb_atma(self, value: Iterable[float] | float):
        """
        Устанавливает массив pb_atma
        :param value: Итерируемый объект, содержащий значения pb_atma
        """
        if not isinstance(value, Iterable):
            self._pb_atma = value
        else:
            self._pb_atma = np.array(value)
