from typing import List, Tuple, Optional
from classes.point import Point
from core.main_function import UfpyCore, UniflocCore


def calculation_of_parameters(module: Optional[UfpyCore, UniflocCore]) -> Tuple[List[float], List[float], List[float]]:
    """
    Данная функция вызывает рассчет параметров с помощью реализаций юнифлок или юфпи
    :param module: объект класса UfpyCore или UniflocCore позволяющий произвести рассчет параметров
    :return: Кортеж списков рассчитанных параметров
    """
    if isinstance(module, (UfpyCore, UniflocCore)):
        bo_m3m3 = module.calculation_parameter("bo")
        rs_m3m3 = module.calculation_parameter("rs")
        pb_atma = module.calculation_parameter("pb")

    else:
        raise TypeError

    return bo_m3m3, rs_m3m3, pb_atma


def checking_calculations(ufpy_points: List[Point], unifloc_points: List[Point], flag: str) -> bool:
    """
    Функция проверяет и сравнивает результаты рассчетов полученные с помощью разных модулей
    :param ufpy_points: Список точек полученных рассчетом модуля ufpy
    :param unifloc_points: Список точек полученных рассчетом модуля unifloc
    :param flag: Точное название атрибута в классе Point
    :return: Булевая переменную обозначающая удволетворимость погрешности рассчета
    """
    if len(ufpy_points) != len(unifloc_points):
        raise ValueError

    for i in range(0, len(ufpy_points) - 1):
        relative_fault = calculation_relative_fault(ufpy_points[i], unifloc_points[i], flag)
        if relative_fault > 5:
            print()
            return False

    return True



def calculation_relative_fault(ufpy_point: Point, unifloc_point: Point, flag: str) -> float:
    """
    В данной функции реализован рассчет относительной погрешности параметра
    :param ufpy_point: Точка содержащая значения полученные в результате рассчетов модуля ufpy
    :param unifloc_point: Точка содержащая значения полученные в результате рассчетов модуля unifloc
    :param flag: Точное название атрибута в классе Point
    :return: Относительная погрешность между рассчетами разных модулей
    """
    absolute_fault = getattr(ufpy_point, f"{flag}") - getattr(unifloc_point, f"{flag}")
    relative_fault = absolute_fault / getattr(ufpy_point, f"{flag}") * 100
    return relative_fault

    # if flag is "bo":
    #     absolute_fault = ufpy_point.bo_m3m3 - unifloc_point.bo_m3m3
    #
    # elif flag is "rs":
    #     absolute_fault = ufpy_point.rs_m3m3 - unifloc_point.rs_m3m3
    #
    # elif flag is "pb":
    #     absolute_fault = ufpy_point.pb_atma - unifloc_point.pb_atma
    #
    # else:
    #     raise ValueError
    #
    # return absolute_fault

def creating_points(testing_data: List[Tuple], bo_m3m3: List[float], rs_m3m3: List[float],
                    pb_atma: List[float]
                    ) -> List[Point]:
    """
    Создание списка объектов класса Point
    :param testing_data: Список с кортежами исходных давлений и температур
    :param bo_m3m3: список с рассчитанными объемными коэффициентами нефти
    :param rs_m3m3: список с рассчитанными газосодержаниями
    :param pb_atma: список с рассчитанными давлениями насыщения
    :return: список содержащий объекты класса Point
    """
    points = list()
    if len(bo_m3m3) == len(testing_data):
        for i in range(0, len(testing_data) - 1):
            current_PT_tuple = testing_data[i]
            point = Point(p_atma=current_PT_tuple[0],
                          t_c=current_PT_tuple[1],
                          bo_m3m3=bo_m3m3[i],
                          rs_m3m3=rs_m3m3[i],
                          pb_atma=pb_atma[i]
                          )
            points.append(point)

    return points
