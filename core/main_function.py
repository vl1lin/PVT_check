from abc import ABC
from typing import List, Tuple

from ufpy.pvt import PVT


class Core(ABC):
    def __init__(self, tested_data: List[Tuple]):
        self.tested_data = tested_data

    def calculation_parameter(self, flag: str) -> List[float]:
        """Расчет параметра при заданных температуре и давлении
        :param flag: передача параметра для расчета
        :return: возвращает список расчетных значений параметра
        """
        parameter_data = []
        for data_tuple in self.tested_data:
            if flag == "rs":
                parameter = self.calculation_rs_m3m3(data_tuple[0], data_tuple[1])

            elif flag == "bo":
                parameter = self.calculation_bo_m3m3(data_tuple[0], data_tuple[1])

            elif flag == "pb":
                parameter = self.calculation_pb_atma(data_tuple[1])

            else:
                raise ValueError

            parameter_data.append(parameter)
        return parameter_data

    def calculation_bo_m3m3(self, p_atma: float, t_c: float) -> float:
        """Расчет объемного коэффициента нефти по известным давлению и температуре
        :param p_atma: давление заданное в атмосферах
        :param t_c: температура заданная в цельсиях
        :return: объемный коэффициент нефти в м3/м3
        """
        ...

    def calculation_rs_m3m3(self, p_atma: float, t_c: float) -> float:
        """Расчет газосодержания при заданных давлении и температуре
        :param p_atma: давление заданное в атмосферах
        :param t_c: температура заданная в цельсиях
        :return: газосодержание в м3/м3
        """
        ...

    def calculation_pb_atma(self, t_c: float, rsb: float = 1) -> float:
        """Расчет давления насыщения по известному газосодержанию при давлении насыщения и температуре
        :param rsb: газосодержание при давлении насыщения
        :param t_c: температура заданная в цельсиях
        :return: давление насыщения нефти в атм
        """
        ...


class UfpyCore(Core):
    def __init__(self, fluid_as_ufpy: PVT, tested_data: List[Tuple]):
        super().__init__(tested_data)
        self.fluid_as_ufpy = fluid_as_ufpy

    def calculation_bo_m3m3(self, p_atma: float, t_c: float) -> float:
        bo_m3m3 = self.fluid_as_ufpy.calc_bo_m3m3(p_atma=p_atma, t_C=t_c)
        return bo_m3m3

    def calculation_rs_m3m3(self, p_atma: float, t_c: float) -> float:
        rs_m3m3 = self.fluid_as_ufpy.calc_rs_m3m3(p_atma=p_atma, t_C=t_c)
        return rs_m3m3

    def calculation_pb_atma(self, t_c: float, rsb: float = 1) -> float:
        pb_atma = self.fluid_as_ufpy.calc_pb_atma(rsb=rsb, t_C=t_c)
        return pb_atma


class UniflocCore(Core):
    def __init__(self, fluid_as_unifloc, unifloc_api, tested_data: List[Tuple]):
        super().__init__(tested_data)
        self.fluid_as_unifloc = fluid_as_unifloc
        self.unifloc_api = unifloc_api

    def calculation_bo_m3m3(self, p_atma: float, t_c: float) -> float:
        bo_m3m3 = self.unifloc_api.PVT_bo_m3m3(
            p_atma=p_atma, t_C=t_c, PVT_json=self.fluid_as_unifloc
        )
        return bo_m3m3

    def calculation_rs_m3m3(self, p_atma: float, t_c: float) -> float:
        rs_m3m3 = self.unifloc_api.PVT_rs_m3m3(
            p_atma=p_atma, t_C=t_c, PVT_json=self.fluid_as_unifloc
        )
        return rs_m3m3

    def calculation_pb_atma(self, t_c: float, rsb: float = 1) -> float:
        pb_atma = self.unifloc_api.PVT_pb_atma(t_C=t_c, PVT_json=self.fluid_as_unifloc)
        return pb_atma
