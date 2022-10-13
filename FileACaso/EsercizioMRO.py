class ClasseA:
    t = 32
    f = 242
    d = "dede"


class ClasseB(ClasseA):
    ciao = "de"
    trf = "ded"
    c = 22
    t = 243

    def contaVarClasse(self, t, n):
        numeroVar = 0
        for i, classe in enumerate(ClasseB.__mro__):
            if i > n:
                return numeroVar

            dizionarioClasse = vars(classe)

            for Nvar in dizionarioClasse:
                if Nvar == "__name__" or Nvar == "__doc__" or Nvar == "__module__":
                    continue

                var = vars(classe).get(Nvar)
                if type(var) == t:
                    numeroVar = numeroVar + 1

        return numeroVar


b = ClasseB()

print(b.contaVarClasse(str, 5))
