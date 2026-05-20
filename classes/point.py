from ufpy.pvt import PVT


class Point(PVT):
    def __init__(
        self,
        **kwargs,
    ):
        super().__init__()
        self.init(**kwargs)
        self._t_c: float
        self._p_atma: float

    @property
    def t_c(self) -> float:
        """Temperature in Celsius"""
        return self._t_c

    @t_c.setter
    def t_c(self, t_c: float):
        self._t_c = t_c

    @property
    def p_atma(self) -> float:
        """Pressure in atmospheres"""
        return self._p_atma

    @p_atma.setter
    def p_atma(self, p_atma: float):
        self._p_atma = p_atma

    @property
    def rs_m3m3(self) -> float:
        """Газосодержание"""
        return self._rs_m3m3

    @rs_m3m3.setter
    def rs_m3m3(self, rs_m3m3: float):
        self._rs_m3m3 = rs_m3m3

    @property
    def bo_m3m3(self) -> float:
        """Объемный коэффициент нефти"""
        return self._bo_m3m3

    @bo_m3m3.setter
    def bo_m3m3(self, bo_m3m3: float):
        self._bo_m3m3 = bo_m3m3

    @property
    def pb_atma(self) -> float:
        """Давление насыщения в атмосферах"""
        return self._pb_atma

    @pb_atma.setter
    def pb_atma(self, pb_atma: float):
        self._pb_atma = pb_atma

    @property
    def rsb_m3m3(self) -> float:
        """Газосодержание при давлении насыщения"""
        return self._rsb_m3m3

    @rsb_m3m3.setter
    def rsb_m3m3(self, rsb_m3m3: float):
        self._rsb_m3m3 = rsb_m3m3
