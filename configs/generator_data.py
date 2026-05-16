from typing import List, Tuple

import numpy as np


class GeneratorDataForTest:
    def __init__(self):
        self.pressure: List[float] | np.ndarray
        self.temperature: List[float] | np.ndarray

    def pipeline(self) -> List[Tuple]:
        """
        Основной метод для генерации данных
        :return: список кортежей (давление, температура)
        """
        self.generate_case()
        return self.wrapping_in_tuple()

    def generate_case(self) -> None:
        """
        Функция генерирует список кортежей для рассчета зависимостей
        Данные сохраняются в атрибуты класса
        :return: None
        """
        pass

    def wrapping_in_tuple(self) -> List[Tuple]:
        """
        Функция оборачивает данные в кортежи
        Работа производится с атрибутами класса, поэтому функция не принимает параметров
        :return: список кортежей (давление, температура)
        """
        wrapped_tuples: List[Tuple] = list()
        for pressure, temperature in zip(self.pressure, self.temperature):
            wrapped_tuples.append((pressure, temperature))
        return wrapped_tuples


class GeneratorPressure(GeneratorDataForTest):
    def __init__(self):
        super().__init__()

    def generate_case(
        self,
        pressure_min: float = 1.0,
        pressure_max: float = 56.0,
        temperature: float = 80.0,
        num_points: int = 100,
    ) -> None:
        """
        Функция генерирует список кортежей для рассчета зависимостей от давления
        Температура принимается величиной постоянным
        :param pressure_min: минимальное давление
        :param pressure_max: максимальное давление
        :param temperature: температура
        :param num_points: количество точек
        :return: None
        """
        self.pressure = np.linspace(pressure_min, pressure_max, num_points)
        self.temperature = [temperature for _ in range(len(self.pressure))]


class GeneratorTemperature(GeneratorDataForTest):
    def __init__(self):
        super().__init__()

    def generate_case(
        self,
        temperature_min: float = 80.0,
        temperature_max: float = 100.0,
        pressure: float = 4.0,
        num_points: int = 100,
    ) -> None:
        """
        Функция генерирует список кортежей для рассчета зависимостей от температуры
        Давление принимается величиной постоянным
        :param temperature_min: минимальная температура
        :param temperature_max: максимальная температура
        :param pressure: давление
        :param num_points: количество точек
        :return: None
        """
        self.temperature = np.linspace(temperature_min, temperature_max, num_points)
        self.pressure = [pressure for _ in range(len(self.temperature))]
