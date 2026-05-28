from dataclasses import dataclass, fields
from typing import Iterable

import numpy as np

PVTArray = np.ndarray | None


@dataclass
class PVTData:
    _p_atma: PVTArray = None
    _t_C: PVTArray = None
    _rsb_m3m3: PVTArray = None

    def keys(self) -> Iterable[str]:
        return (f.name[1:] for f in fields(self) if getattr(self, f.name) is not None)

    def __getitem__(self, key: str) -> list:
        if key not in self.keys():
            raise KeyError(f"Invalid key: {key}")
        value = getattr(self, f"_{key}")
        if value is None:
            raise ValueError(f"{key} is None")
        return value.tolist()

    @property
    def p_atma(self) -> np.ndarray:
        """Возвращает массив давления в атмосферах"""
        if self._p_atma is None:
            raise ValueError("p_atma is None")
        return self._p_atma

    @p_atma.setter
    def p_atma(self, array: np.ndarray) -> None:
        if self._p_atma is not None:
            print("p_atma is already set")
            return
        self._p_atma = array

    def set_p_atma_linspace(self, min: float, max: float, count: int) -> None:
        """Устанавливает давление через np.linspace"""
        self._p_atma = np.linspace(min, max, count)

    @property
    def t_C(self) -> np.ndarray:
        """Возвращает массив температуры в градусах Цельсия"""
        if self._t_C is None:
            raise ValueError("t_c is None")
        return self._t_C

    @t_C.setter
    def t_C(self, array: np.ndarray) -> None:
        if self._t_C is not None:
            print("t_C is already set")
            return
        self._t_C = array

    def set_t_C_linspace(self, min: float, max: float, count: int) -> None:
        """Устанавливает температуру через np.linspace"""
        self._t_C = np.linspace(min, max, count)

    @property
    def rsb_m3m3(self) -> np.ndarray:
        """Возвращает массив плотности газа"""
        if self._rsb_m3m3 is None:
            raise ValueError("rsb_m3m3 is None")
        return self._rsb_m3m3

    @rsb_m3m3.setter
    def rsb_m3m3(self, array: np.ndarray) -> None:
        if self._rsb_m3m3 is not None:
            print("rsb_m3m3 is already set")
            return
        self._rsb_m3m3 = array

    def set_rsb_m3m3_linspace(self, min: float, max: float, count: int) -> None:
        """Устанавливает плотность газа через np.linspace"""
        self._rsb_m3m3 = np.linspace(min, max, count)
