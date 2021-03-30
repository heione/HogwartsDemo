from study.rewrite.A import A


class B(A):
    def run_t(self):
        print(f"我是子类的run，重写了父类")


B().run_t()
