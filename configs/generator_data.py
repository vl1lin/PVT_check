from abc import ABC, abstractmethod
from dataclasses import fields
from typing import List

import numpy as np

from classes.point import Point
from configs.default import DefaultConfig


class GeneratorDataForTest(ABC):
    def __init__(self, data_config: DefaultConfig, constant_parameter: float):
        self.data_config: DefaultConfig = data_config
        self.constant_parameter: float = constant_parameter
        self.points: List[Point] = list()

    def pipeline(self, min: float, max: float, count_of_points: int) -> List[Point]:
        """
        Основной метод для генерации данных
        :param min: минимальное значение параметра
        :param max: максимальное значение параметра
        :param count_of_points: количество точек
        :return: список объектов класса Point
        """
        changeable_parameter = self.generate_case(min, max, count_of_points)
        general_data = self.getting_data_from_config()
        for value in changeable_parameter:
            point = Point(**general_data)
            self.add_changeable_and_constant_parameters(value, point)
            self.points.append(point)
        return self.points

    def getting_data_from_config(self) -> dict[str, float]:
        """
        Функция создает словарь данных из конфигурационного класса
        :return: словарь данных dict[str, float]
        """
        data_from_config: dict[str, float] = {}
        for i in fields(self.data_config):
            if i.name == "pvt_corr_set":
                continue
            value = getattr(self.data_config, i.name)
            data_from_config[i.name] = value
        return data_from_config

    @abstractmethod
    def add_changeable_and_constant_parameters(
        self, changeable_parameter: float, point: Point
    ) -> None:
        """
        Функция добавляет изменяемый параметр к точке
        :param changeable_parameter: изменяемый параметр
        :param constant_parameter: постоянный параметр
        :param point: объект Point
        """
        ...

    @abstractmethod
    def generate_case(self, min: float, max: float, count_of_points: int) -> np.ndarray:
        """
        Функция генерирует список для изменяемого параметра объекта Point
        :param min: минимальное значение параметра
        :param max: максимальное значение параметра
        :param count_of_points: количество точек
        :return: массив numpy (ndarray)
        """
        ...


class GeneratorPressure(GeneratorDataForTest):
    def __init__(self, data_config: DefaultConfig, constant_parameter: float):
        super().__init__(data_config, constant_parameter)

    def generate_case(self, min: float, max: float, count_of_points: int) -> np.ndarray:
        """
        Функция генерирует список для давления
        :param min: минимальное значение параметра
        :param max: максимальное значение параметра
        :param count_of_points: количество точек
        :return: массив numpy (ndarray)
        """
        pressure = np.linspace(min, max, count_of_points)
        return pressure

    def add_changeable_and_constant_parameters(
        self, changeable_parameter: float, point: Point
    ) -> None:
        """
        Функция добавляет изменяемый парметр (давление) и постоянный параметр (температуру) к точке
        :param changeable_parameter: изменяемый параметр
        :param point: объект Point
        """
        point.p_atma = changeable_parameter
        point.t_c = self.constant_parameter
