from study.rewrite import warp


class A:
    @warp.warpper
    @warp.warpper1
    def run_t(self):
        pass


A().run_t()
