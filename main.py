from configs.default import DefaultConfig
from configs.generator_data import GeneratorPressure, GeneratorRSB
from core.runner import ComparisonRunner


def main() -> None:
    config = DefaultConfig(
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

    runner = ComparisonRunner(config)

    # Сценарий 1: варьируем газосодержание при насыщении (rsb) при фиксированных p=50 атм, t=80°C
    gen_rsb = GeneratorRSB(config, constant_parameter=(50.0, 80.0))
    runner.run(
        generator=gen_rsb,
        min_val=100,
        max_val=500,
        n_points=100,
        x_parameter="rsb_m3m3",
        x_label="Газосодержание при давлении насыщения, м³/м³",
        plot_title="Сравнение unfpy vs unifloc — варьирование Rsb",
        save_path="comparison_rsb.png",
    )

    # Сценарий 2: варьируем давление при фиксированных rsb=120 м³/м³, t=80°C
    gen_p = GeneratorPressure(config, constant_parameter=80.0)
    runner.run(
        generator=gen_p,
        min_val=10,
        max_val=200,
        n_points=100,
        x_parameter="p_atma",
        x_label="Давление, атм",
        plot_title="Сравнение unfpy vs unifloc — варьирование давления",
        save_path="comparison_pressure.png",
    )


if __name__ == "__main__":
    main()
