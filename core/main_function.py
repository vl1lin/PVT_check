from abc import ABC
from typing import List, Tuple

import unifloc_vba_python_api.python_api as unifloc
from ufpy.pvt import PVT

from classes.point import Point


class Core(ABC):
    def __init__(
        self,
        tested_data: List[Tuple],
        fluid_as_ufpy: PVT = None,
        fluid_as_unifloc: unifloc.Fluid = None,
        unifloc_api: unifloc.API = None,
    ):
        self.tested_data = tested_data
        self.fluid_as_ufpy: PVT = fluid_as_ufpy
        self.fluid_as_unifloc: unifloc.Fluid = fluid_as_unifloc
        self.unifloc_api: unifloc.API = unifloc_api
        self.points: List[Point] = []

    def pipeline(self) -> None:
        """
        Основной пайплайн для выполнения расчетов.
        Выполняет последовательно методы making_points и calculation_parameter.
        """
        self.making_points()
        self.calculation_parameter()

    def making_points(self) -> None:
        """
        Создание точек на основе тестовых данных
        :return: функция ничего не возвращает, она наполняет спосок points объектами класса Point
        """
        ...

    def calculation_parameter(self) -> None:
        """Расчет параметров при заданных температуре и давлении
        :return: Функция ничего не возвращает, она изменяет объекты Point в списке points
        """
        ...


class UfpyCore(Core):
    def __init__(self, fluid_as_ufpy: PVT, tested_data: List[Tuple]):
        super().__init__(tested_data, fluid_as_ufpy=fluid_as_ufpy)

    def making_points(self) -> None:
        for tuple_pt in self.tested_data:
            point = Point(
                p_atma=tuple_pt[0],
                t_c=tuple_pt[1],
                gamma_gas=self.fluid_as_ufpy.gamma_g,
                gamma_oil=self.fluid_as_ufpy.gamma_o,
                gamma_wat=self.fluid_as_ufpy.gamma_w,
                rsb_m3m3=self.fluid_as_ufpy.rsb_m3m3,
                pb_atma=self.fluid_as_ufpy.pb_atma,
                bob_m3m3=self.fluid_as_ufpy.bob_m3m3,
                muob_cP=self.fluid_as_ufpy.muob_cP,
                t_res_C=self.fluid_as_ufpy.t_res_C,
            )
            self.points.append(point)

    def calculation_parameter(self) -> None:
        for point in self.points:
            point.calc_pvt(point.p_atma, point.t_c)


class UniflocCore(Core):
    def __init__(
        self,
        fluid_as_unifloc: unifloc.Fluid,
        unifloc_api: unifloc.API,
        tested_data: List[Tuple],
    ):
        super().__init__(
            tested_data, fluid_as_unifloc=fluid_as_unifloc, unifloc_api=unifloc_api
        )

    def making_points(self) -> None:
        for tuple_pt in self.tested_data:
            fluid = self.unifloc_api.PVT_calc(
                p_atma=tuple_pt[0], t_C=tuple_pt[1], PVT_json=self.fluid_as_unifloc
            )
            parameters = self.unifloc_api.decode_json(json=fluid)
            point = Point(p_atma=tuple_pt[0], t_c=tuple_pt[1])
            for item in parameters:
                if item[0] == "rs_m3m3":
                    point.unifloc_rs_m3m3 = item[1]
                elif item[0] == "bo_m3m3":
                    point.unifloc_bo_m3m3 = item[1]
                elif item[0] == "pb_atma":
                    point.unifloc_pb_atma = item[1]
                elif item[0] == "rsb_m3m3":
                    point.unifloc_rsb_m3m3 = item[1]
            self.points.append(point)

    def calculation_parameter(self) -> None:
        pass
