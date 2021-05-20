from HogwartsDemo.study.rewrite import warp
from HogwartsDemo.study.rewrite.B import B


class C(B):
    # @warp.warpper
    def run_t(self):
        print("我是C，继承了B")
