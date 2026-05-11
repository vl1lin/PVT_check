from typing import List

import matplotlib.pyplot as plt

from classes.point import Point


class Plot:
    def __init__(self, points_ufpy: list[Point], points_unifloc: List[Point]):
        self._points_ufpy = points_ufpy
        self._points_unifloc = points_unifloc

    def create_plot(self) -> None:
        fig, ax = plt.subplots()

        ax.plot(
            [p.p_atma for p in self._points_ufpy],
            [p.t_c for p in self._points_ufpy],
            label="UFPY",
        )
        ax.plot(
            [p.p_atma for p in self._points_ufpy],
            [p.t_c for p in self._points_unifloc],
            label="Unifloc",
        )

        ax.set_xlabel("Pressure (atm)")
        ax.set_ylabel("Temperature (C)")
        ax.legend()
        plt.show()

    def save_plot(self) -> None:
        pass
