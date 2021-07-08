def a_warpper(fun):
    def f(*args):
        return fun(*args)
    return f
