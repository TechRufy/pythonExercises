"""
Scrivere un decorator factory che prende in input una classe ClasseConFFe due stringhe funz e delegata e
restituisce un decoratore di classe che decora una classe in modo tale che se viene invocata funz di fatto
al posto di funz viene invocata la funzione ff della classe ClasseConFF.
"""


class ClasseConFF:

    def ff(self):
        print("ciao prova ciao")


def DecoratorFactory(clsFF, funz):
    def Decorating(cls):
        setattr(cls, funz, clsFF.ff)

        return cls

    return Decorating


@DecoratorFactory(ClasseConFF, "boh")
class Classeprova:

    def boh(self):
        print("boh")


t = Classeprova()
t.boh()
