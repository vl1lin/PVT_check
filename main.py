import numpy as np

from core.compare_core import CompareCore
from data.config_data import Data
from data.pvt_data import PVTData
from visualisation.graphs_core import GraphsCore


def main() -> None:

    dataset = Data(
        gamma_oil=0.8,
        gamma_wat=1,
        gamma_gas=0.4,
        PVT_corr_set=0,
    )

    pvt_data = PVTData()
    pvt_data.set_p_atma_linspace(1, 300, 100)
    pvt_data.t_C = np.array([80 for _ in range(100)])
    pvt_data.set_rsb_m3m3_linspace(1, 500, 100)
    compare = CompareCore(dataset, pvt_data)
    graphs = GraphsCore(compare, pvt_data)

    graphs.plot_rs()  # только Rs
    graphs.plot_bo()  # только Bo
    graphs.plot_pb()  # только Pb
    # graphs.plot_all("all.png")  # все три сразу


if __name__ == "__main__":
    main()
