class MyClass:

    def __init__(self, x):
        self.x = x

    def f(self):
        print("ciao sono f e la variabile e' " + self.x)


class MyProxy:

    def __init__(self, x):
        self.__implementation = MyClass(x)

    def __getattr__(self, item):
        return getattr(self.__implementation, item)


P = MyProxy("ciao")

P.f()
