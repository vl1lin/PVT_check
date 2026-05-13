from typing import List

import matplotlib.pyplot as plt

from classes.point import Point


class Plot:
    def __init__(self, points_ufpy: List[Point], points_unifloc: List[Point]):
        self._points_ufpy = points_ufpy
        self._points_unifloc = points_unifloc
        self.fig, self.ax = plt.subplots()

    def create_subplot(self) -> None:
        """
        Метод создает график сравнения результатов UFPY и Unifloc
        :return: Ничего не возвращает, только отоброжает график
        """
        pass

    def create_plot(
        self,
        nums_for_x: List[float],
        nums_for_y: List[float],
        label: str,
        xlabel: str,
        ylabel: str,
    ) -> None:
        """
        Метод создает график
        :param nums_for_x: список значений оси X
        :param nums_for_y: список значений оси Y
        :param label: название графика
        :param xlabel: название оси X
        :param ylabel: название оси Y
        :return: Ничего не возвращает, только добавляет график
        """

        self.ax.plot(nums_for_x, nums_for_y, label=label)

        self.ax.set_xlabel(xlabel)
        self.ax.set_ylabel(ylabel)

    def getting_parameters_from_points(
        self, points: List[Point], flag: str
    ) -> List[float]:
        """
        Метод получает из списка точек значение указанного параметра
        :param points: список точек
        :param frag: название параметра
        :return: список значений параметра
        """
        parameter: List[float] = list()
        for point in points:
            parameter.append(getattr(point, flag))
        return parameter

    def save_plot(self) -> None:
        pass


class PlotBo(Plot):
    def __init__(self, points_ufpy: List[Point], points_unifloc: List[Point]):
        super().__init__(points_ufpy, points_unifloc)

    def create_subplot(self) -> None:

        ufpy_nums_for_x = self.getting_parameters_from_points(
            self._points_ufpy, "p_atma"
        )
        ufpy_nums_for_y = self.getting_parameters_from_points(
            self._points_ufpy, "bo_m3m3"
        )
        self.create_plot(
            ufpy_nums_for_x,
            ufpy_nums_for_y,
            "UFPY",
            xlabel="Pressure (atm)",
            ylabel="B_m3m3",
        )

        unifloc_nums_for_x = self.getting_parameters_from_points(
            self._points_unifloc, "p_atma"
        )
        unifloc_nums_for_y = self.getting_parameters_from_points(
            self._points_unifloc, "bo_m3m3"
        )
        self.create_plot(
            unifloc_nums_for_x,
            unifloc_nums_for_y,
            "Unifloc",
            xlabel="Pressure (atm)",
            ylabel="B_m3m3",
        )
        plt.show()


class PlotRs(Plot):
    def __init__(self, points_ufpy: List[Point], points_unifloc: List[Point]):
        super().__init__(points_ufpy, points_unifloc)

    def create_subplot(self) -> None:

        ufpy_nums_for_x = self.getting_parameters_from_points(
            self._points_ufpy, "p_atma"
        )
        ufpy_nums_for_y = self.getting_parameters_from_points(
            self._points_ufpy, "rs_m3m3"
        )
        self.create_plot(
            ufpy_nums_for_x,
            ufpy_nums_for_y,
            "UFPY",
            xlabel="Pressure (atm)",
            ylabel="Rs_m3m3",
        )

        unifloc_nums_for_x = self.getting_parameters_from_points(
            self._points_unifloc, "p_atma"
        )
        unifloc_nums_for_y = self.getting_parameters_from_points(
            self._points_unifloc, "rs_m3m3"
        )
        self.create_plot(
            unifloc_nums_for_x,
            unifloc_nums_for_y,
            "Unifloc",
            xlabel="Pressure (atm)",
            ylabel="Rs_m3m3",
        )

        plt.show()


class PlotPb(Plot):
    def __init__(self, points_ufpy: List[Point], points_unifloc: List[Point]):
        super().__init__(points_ufpy, points_unifloc)

    def create_subplot(self) -> None:

        ufpy_nums_for_x = self.getting_parameters_from_points(
            self._points_ufpy, "rs_m3m3"
        )
        ufpy_nums_for_y = self.getting_parameters_from_points(
            self._points_ufpy, "pb_atma"
        )
        self.create_plot(
            ufpy_nums_for_x,
            ufpy_nums_for_y,
            "UFPY",
            xlabel="Rs_m3m3",
            ylabel="Pb_atma",
        )

        unifloc_nums_for_x = self.getting_parameters_from_points(
            self._points_unifloc, "rs_m3m3"
        )
        unifloc_nums_for_y = self.getting_parameters_from_points(
            self._points_unifloc, "pb_atma"
        )
        self.create_plot(
            unifloc_nums_for_x,
            unifloc_nums_for_y,
            "Unifloc",
            xlabel="Rs_m3m3",
            ylabel="Pb_atma",
        )
        plt.show()
