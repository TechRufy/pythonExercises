class Bambino:
    stati = ["iscritto", "alSecondoAnno", "alTerzoAnno", "Diplomato"]

    def stampaStato(self):
        pass

    def __init__(self):
        self.state = 0

    def stampaStato(self):
        pass

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state):
        self.stampaStato = lambda: print("Il bambino e` nello stato " + Bambino.stati[state])
        self._state = state

    def succ(self):
        if self.state >= 3 or self.state < 0:
            print("il bambino e' nello stato " + Bambino.stati[self.state] + " e non può avanzare")
        else:
            self.state = self.state + 1

    def pred(self):
        if self.state <= 0 or self.state > 3:
            print("il bambino e' nello stato " + Bambino.stati[self.state] + " e non può tornare indietro")
        else:
            self.state = self.state - 1

    def salta_anno(self):
        if self.state >= 2 or self.state < 0:
            print("il bambino e' nello stato " + Bambino.stati[self.state] + " e non può saltare un anno")
        else:
            self.state = self.state + 2


def main():
    bambino = Bambino()
    bambino.stampaStato()
    bambino.pred()
    bambino.succ()
    bambino.stampaStato()
    bambino.succ()
    bambino.stampaStato()
    bambino.salta_anno()
    bambino.succ()
    bambino.stampaStato()
    bambino.succ()


if __name__ == "__main__":
    main()

"""IL programma deve stampare:

Il bambino e` nello stato  iscritto
Il bambino  e` appena stato iscritto al I anno e non puo` tornare in uno stato precedente
Il bambino e` nello stato  alSecondoAnno
Il bambino e` nello stato  alTerzoAnno
Il bambino e` nello stato alTerzoAnno  e non puo` saltare un anno
Il bambino e` nello stato  diplomato
Il bambino  si e` gia` diplomato e non puo` avanzare in uno stato successivo
"""
