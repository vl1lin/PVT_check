from abc import ABC, abstractmethod
from typing import List, Tuple

import unifloc_vba_python_api.python_api as unifloc

from classes.point import Point


class Core(ABC):
    def __init__(
        self,
        points: List[Point],
        fluid_as_unifloc: unifloc.Fluid = None,
        unifloc_api: unifloc.API = None,
    ):
        self.fluid_as_unifloc: unifloc.Fluid = fluid_as_unifloc
        self.unifloc_api: unifloc.API = unifloc_api
        self.points: List[Point] = points

    def pipeline(self) -> List[Point]:
        """
        Основной пайплайн для выполнения расчетов.
        """
        for point in self.points:
            self.calculation_parameters(point)
        return self.points

    @abstractmethod
    def calculation_parameters(
        self, point: Point
    ) -> None | Tuple[Tuple[str, str], ...]:
        """Расчет параметров при заданных температуре и давлении
        :return: Функция ничего не возвращает, она изменяет объекты Point в списке points
        """
        ...


class UfpyCore(Core):
    def __init__(self, points: List[Point]):
        super().__init__(points)

    def pipeline(self) -> List[Point]:
        return super().pipeline()

    def calculation_parameters(self, point: Point) -> None:
        point.calc_pvt(point.p_atma, point.t_c)


class UniflocCore(Core):
    def __init__(
        self,
        points: List[Point],
        fluid_as_unifloc: unifloc.Fluid,
        unifloc_api: unifloc.API,
    ):
        super().__init__(
            points=points, fluid_as_unifloc=fluid_as_unifloc, unifloc_api=unifloc_api
        )

    def pipeline(self) -> List[Point]:
        for point in self.points:
            parameters = self.calculation_parameters(point)
            assert parameters is not None
            self.changing_point(point, parameters)
        return self.points

    def changing_point(
        self, point: Point, parameters: Tuple[Tuple[str, str], ...]
    ) -> None:
        for item in parameters[:3]:
            setattr(point, item[0], float(item[1]))

    def calculation_parameters(self, point: Point) -> Tuple[Tuple[str, str], ...]:
        fluid = self.unifloc_api.PVT_calc(
            p_atma=point.p_atma, t_C=point.t_c, PVT_json=self.fluid_as_unifloc
        )
        parameters = self.unifloc_api.decode_json(json=fluid)
        return parameters
