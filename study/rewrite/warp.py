def warpper(func):
    def f(*args):
        print(f"我是装饰器输出")
        return func(*args)
    return f


def warpper1(func):
    def f(*args):
        print(f"我是装饰器输出11111111")
        return func(*args)
    return f
