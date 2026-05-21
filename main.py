from classes.plot import PlotBo, PlotPb, PlotRs
from configs.default import DefaultConfig
from configs.generator_data import GeneratorPressure, GeneratorRSB
from core.main_function import UfpyCore, UniflocCore
from core.technical_function import checking_calculations


def main() -> None:
    test_data = DefaultConfig(
        gamma_gas=0.75,
        gamma_oil=0.86,
        gamma_wat=1,
        rsb_m3m3=120,
        pb_atma=10,
        t_res_C=90,
        bob_m3m3=100,
        muob_cP=5,
        pvt_corr_set=0,
    )

    t_c = 80
    p_atma = 50
    # main_object = GeneratorPressure(test_data, t_c)
    main_object = GeneratorRSB(test_data, (p_atma, t_c))
    # points = main_object.pipeline(min=1, max=100, count_of_points=2)
    points = main_object.pipeline(min=1, max=50, count_of_points=100)

    ufpy = UfpyCore(points)
    unifloc = UniflocCore(
        points=points,
        fluid_as_unifloc=test_data.initiate_unifloc(),
        unifloc_api=test_data.initiate_unifloc_api(),
    )

    ufpy.pipeline()
    unifloc.pipeline()

    # success_bo = checking_calculations(ufpy.points, unifloc.points, "bo_m3m3")
    # success_rs = checking_calculations(ufpy.points, unifloc.points, "rs_m3m3")
    # success_pb = checking_calculations(ufpy.points, unifloc.points, "pb_atma")

    # print(f"Удволетворимость рассчета bo: {success_bo}")
    # print(f"Удволетворимость рассчета rs: {success_rs}")
    # print(f"Удволетворимость рассчета pb: {success_pb}")

    for i, k in zip(ufpy.points, unifloc.points):
        print(i.rsb_m3m3, i.pb_atma)
        print(k.rsb_m3m3, k.pb_atma)

    # plot_bo = PlotBo(ufpy.points, unifloc.points)
    # plot_bo.create_subplot()
    # plot_rs = PlotRs(ufpy.points, unifloc.points)
    # plot_rs.create_subplot()
    plot_pb = PlotPb(ufpy.points, unifloc.points)
    plot_pb.create_subplot()


if __name__ == "__main__":
    main()
