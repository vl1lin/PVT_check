from typing import List

from classes.point import Point


def checking_calculations(
    ufpy_points: List[Point], unifloc_points: List[Point], flag: str
) -> bool:
    """
    Функция проверяет и сравнивает результаты рассчетов полученные с помощью разных модулей
    :param ufpy_points: Список точек полученных рассчетом модуля ufpy
    :param unifloc_points: Список точек полученных рассчетом модуля unifloc
    :param flag: Точное название атрибута в классе Point
    :return: Булевая переменную обозначающая удволетворимость погрешности рассчета
    """
    if len(ufpy_points) != len(unifloc_points):
        raise ValueError("Списки точек должны быть одинаковой длины")

    for i in range(0, len(ufpy_points)):
        relative_fault = calculation_relative_fault(
            ufpy_points[i], unifloc_points[i], flag
        )
        if relative_fault > 5:
            print(f"Погрешность рассчета превышает допустимый порог в 5% на точке {i}")
            return False

    return True


def calculation_relative_fault(
    ufpy_point: Point, unifloc_point: Point, flag: str
) -> float:
    """
    В данной функции реализован рассчет относительной погрешности параметра
    :param ufpy_point: Точка содержащая значения полученные в результате рассчетов модуля ufpy
    :param unifloc_point: Точка содержащая значения полученные в результате рассчетов модуля unifloc
    :param flag: Точное название атрибута в классе Point
    :return: Относительная погрешность между рассчетами разных модулей
    """
    absolute_fault = getattr(ufpy_point, f"{flag}") - getattr(unifloc_point, f"{flag}")
    relative_fault = abs(absolute_fault / getattr(ufpy_point, f"{flag}") * 100)
    return relative_fault
