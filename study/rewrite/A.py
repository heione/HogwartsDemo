from HogwartsDemo.study.rewrite import warp


class A:
    def start(self):
        self.run_t()

    @warp.warpper
    def run_t(self):
        pass
