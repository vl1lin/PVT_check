from abc import ABC, abstractmethod

import numpy as np


class BaseCore(ABC):
    @abstractmethod
    def calculate_rs(
        self,
    ) -> np.ndarray:
        """Рассчитывает газосодержание
        :return: возвращает массив газосодержания
        """
        ...

    @abstractmethod
    def calculate_pb(self) -> np.ndarray:
        """Рассчитывает давление насыщения
        :return: возвращает массив давления насыщения
        """
        ...

    @abstractmethod
    def calculate_bo(self) -> np.ndarray:
        """Рассчитывает объемный коэффициент
        :return: возвращает массив объемного коэффициента
        """
        ...
