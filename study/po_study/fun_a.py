from study.po_study import funa_warpper
from study.po_study.fun_b import Fun_B


class Fun_A:
    @funa_warpper.a_warpper
    def fun_a(self):
        print("fun_a")
        return Fun_B()
