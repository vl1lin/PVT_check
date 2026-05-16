from classes.plot import PlotBo, PlotPb, PlotRs
from configs.default import Config, DefaultConfig
from configs.generator_data import GeneratorPressure
from core.main_function import UfpyCore, UniflocCore
from core.technical_function import checking_calculations


def main() -> None:
    data_for_test = GeneratorPressure().pipeline()
    test_data = DefaultConfig(
        gamma_gas=0.75,
        gamma_oil=0.86,
        gamma_wat=1,
        rsb_m3m3=120,
        pb_atma=10,
        t_res_c=90,
        bob_m3m3=100,
        muob_cp=5,
        pvt_corr_set=0,
    )
    test_config = Config(
        name="fluid", data_fluid=test_data, data_for_test=data_for_test
    )

    ufpy = UfpyCore(
        tested_data=test_config.tested_data, fluid_as_ufpy=test_config.fluid_as_ufpy
    )
    unifloc = UniflocCore(
        tested_data=test_config.tested_data,
        fluid_as_unifloc=test_config.fluid_as_unifloc,
        unifloc_api=test_config.unifloc_api,
    )

    ufpy.pipeline()
    unifloc.pipeline()

    success_bo = checking_calculations(ufpy.points, unifloc.points, "bo_m3m3")
    success_rs = checking_calculations(ufpy.points, unifloc.points, "rs_m3m3")
    success_pb = checking_calculations(ufpy.points, unifloc.points, "pb_atma")

    print(f"Удволетворимость рассчета bo: {success_bo}")
    print(f"Удволетворимость рассчета rs: {success_rs}")
    print(f"Удволетворимость рассчета pb: {success_pb}")

    plot_bo = PlotBo(ufpy.points, unifloc.points)
    plot_bo.create_subplot()
    plot_rs = PlotRs(ufpy.points, unifloc.points)
    plot_rs.create_subplot()
    plot_pb = PlotPb(ufpy.points, unifloc.points)
    plot_pb.create_subplot()


if __name__ == "__main__":
    main()
