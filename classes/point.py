from ufpy.pvt import PVT


class Point(PVT):
    def __init__(
        self,
        t_c: float,
        p_atma: float,
        unifloc_rs_m3m3: float | None = None,
        unifloc_bo_m3m3: float | None = None,
        unifloc_pb_atma: float | None = None,
        unifloc_rsb_m3m3: float | None = None,
        **kwargs,
    ):
        super().__init__()
        self.init(**kwargs)
        self.t_c = t_c
        self.p_atma = p_atma
        self.unifloc_rs_m3m3 = unifloc_rs_m3m3
        self.unifloc_bo_m3m3 = unifloc_bo_m3m3
        self.unifloc_pb_atma = unifloc_pb_atma
        self.unifloc_rsb_m3m3 = unifloc_rsb_m3m3
