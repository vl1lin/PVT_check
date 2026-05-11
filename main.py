from classes.plot import PlotBo, PlotPb, PlotRs
from configs.default import Config, DefaultConfig
from core.main_function import UfpyCore, UniflocCore
from core.technical_function import (
    calculation_of_parameters,
    checking_calculations,
    creating_points,
)


def main() -> None:
    data_for_test = [
        (2, 30),
        (3, 40),
        (2.5, 35),
        (3.5, 45),
        (4, 50),
        (4.5, 55),
        (5, 60),
    ]
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

    parameters_ufpy = calculation_of_parameters(ufpy)
    parameters_unifloc = calculation_of_parameters(unifloc)

    points_ufpy = creating_points(
        testing_data=data_for_test, parameters=parameters_ufpy
    )
    points_unifloc = creating_points(
        testing_data=data_for_test, parameters=parameters_unifloc
    )

    success_bo = checking_calculations(
        ufpy_points=points_ufpy, unifloc_points=points_unifloc, flag="bo_m3m3"
    )
    success_rs = checking_calculations(
        ufpy_points=points_ufpy, unifloc_points=points_unifloc, flag="rs_m3m3"
    )
    success_pb = checking_calculations(
        ufpy_points=points_ufpy, unifloc_points=points_unifloc, flag="pb_atma"
    )

    print(success_rs and success_bo)
    # print(*(i.pb_atma for i in points_ufpy))
    # print("-" * 50)
    # print(*(i.pb_atma for i in points_unifloc))

    plot_bo = PlotBo(points_ufpy=points_ufpy, points_unifloc=points_unifloc)
    plot_bo.create_subplot()

    plot_rs = PlotRs(points_ufpy=points_ufpy, points_unifloc=points_unifloc)
    plot_rs.create_subplot()

    plot_pb = PlotPb(points_ufpy=points_ufpy, points_unifloc=points_unifloc)
    plot_pb.create_subplot()


if __name__ == "__main__":
    main()
