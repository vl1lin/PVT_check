from dataclasses import dataclass, fields
from typing import Iterable

import numpy as np

PVTArray = np.ndarray | None


@dataclass
class PVTData:
    _p_atma: PVTArray = None
    _t_C: PVTArray = None

    def keys(self) -> Iterable[str]:
        return (f.name[1:] for f in fields(self))

    def __getitem__(self, key: str) -> np.ndarray:
        if key not in self.keys():
            raise KeyError(f"Invalid key: {key}")
        value = getattr(self, f"_{key}")
        if value is None:
            raise ValueError(f"{key} is None")
        return value

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
    def t_c(self) -> np.ndarray:
        """Возвращает массив температуры в градусах Цельсия"""
        if self._t_c is None:
            raise ValueError("t_c is None")
        return self._t_c

    @t_c.setter
    def t_c(self, array: np.ndarray) -> None:
        if self._t_c is not None:
            print("t_c is already set")
            return
        self._t_c = array

    def set_t_c_linspace(self, min: float, max: float, count: int) -> None:
        """Устанавливает температуру через np.linspace"""
        self._t_c = np.linspace(min, max, count)
