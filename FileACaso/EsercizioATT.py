"""
Scrivere una classe C per cui accade che ogni volta che si aggiunge una variabile d'istanza a una delle istanze di C
in realtà la variabile viene aggiunta alla classe come variabile di classe.
"""


class C:

    def __setattr__(self, key, value):
        return setattr(C, key, value)


c = C()

c.variabileIstanza = 100

print(C.variabileIstanza)
