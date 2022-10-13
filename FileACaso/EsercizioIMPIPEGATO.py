class Impiegato:
    numIStanze = 0

    def __init__(self):
        Impiegato.numIStanze = Impiegato.numIStanze + 1

    @classmethod
    def StampaIstanza(cls):
        print(cls.numIStanze)


class Tecnico(Impiegato):
    numIStanze = 0

    def __init__(self):
        Tecnico.numIStanze += 1
        super().__init__()


class Amministrativo(Impiegato):
    numIStanze = 0

    def __init__(self):
        Amministrativo.numIStanze += 1
        super().__init__()


i = Impiegato()
t = Impiegato()
a = Amministrativo()
p = Tecnico()
c = Amministrativo()

i.StampaIstanza()
c.StampaIstanza()
p.StampaIstanza()
