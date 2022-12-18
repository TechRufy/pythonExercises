import collections
from datetime import date
import copy
import itertools
import random


class ProdottoOsservato:
    M = "altamente disponibile"
    D = "disponibile"
    E = "non disponibile"

    MAXSCORTE = 1000
    MAXORDINE = 350

    @property
    def stato_scorte(self):
        if self.vendi == self._vendiE:
            return ProdottoOsservato.E
        elif self.immagazzina == self._immagazzinaM:
            return ProdottoOsservato.M
        else:
            return ProdottoOsservato.D

    @stato_scorte.setter
    def stato_scorte(self, state):
        if state == ProdottoOsservato.E:
            self.vendi = self._vendiE
            self.immagazzina = self._immagazzina
        elif state == ProdottoOsservato.D:
            self.vendi = self._vendi
            self.immagazzina = self._immagazzina
        elif state == ProdottoOsservato.M:
            self.vendi = self._vendi
            self.immagazzina = self._immagazzinaM
        self.observers_notify("S")

    def __init__(self, nome):
        self.vendi = None
        self.immagazzina = None
        self.quantita = 0
        self._observers = set()
        self.stato_scorte = ProdottoOsservato.E
        self._acquirenti = collections.defaultdict(tuple)
        self.nome = nome

    def observers_add(self, observer, *observers):
        for observer in itertools.chain((observer,), observers):
            self._observers.add(observer)
            # Decidere voi cosa passare ad update (al posto dei puntini)
            observer.update(self, "")

    def observer_discard(self, observer):
        self._observers.discard(observer)

    # completare questo metodo che notifica un cambio stato agli ossservatori invocando il metodo update dell'osservatore
    def observers_notify(self, tipo_azione):
        for observer in self._observers:
            observer.update(self, tipo_azione)

    def aggiorna(self, nome, numero, data):
        if nome not in self._acquirenti.keys():
            self.observers_notify("N")
        self._acquirenti[nome] = (numero, data)


    def _vendiE(self, nomeAcquirente, numero):
        pass

    def _immagazzinaM(self, numero):
        pass

    def _vendi(self, nomeAcquirente, numero):
        if numero > ProdottoOsservato.MAXORDINE or numero > self.quantita:
            print("Attenzione: vendita di {} unita` del prodotto {} non possibile".format(numero, self.nome))
            return
        else:
            self.quantita = self.quantita - numero
            self.observers_notify("V")
            self.aggiorna(nomeAcquirente, numero, date.today())
            if self.quantita == 0:
                self.stato_scorte = ProdottoOsservato.E
            if 0 < self.quantita < ProdottoOsservato.MAXSCORTE:
                self.stato_scorte = ProdottoOsservato.D

    def _immagazzina(self, numero):
        if numero <= 0:
            return
        self.quantita = self.quantita + numero
        self.observers_notify("IM")
        if 0 < self.quantita < ProdottoOsservato.MAXSCORTE:
            self.stato_scorte = ProdottoOsservato.D
        if self.quantita == ProdottoOsservato.MAXSCORTE:
            self.stato_scorte = ProdottoOsservato.M

    # serve per il test in esercizio1.py se usate questa classe anche nell'esercizio 1
    def elimina_scorte(self):
        self.quantita = 0
        self.stato_scorte = ProdottoOsservato.E


# completare le due seguenti classi
class Grossista:

    def __init__(self, nome: str, listaprodotti: list):
        self.nome = nome
        self.prodotti = list()
        for p in listaprodotti:
            self.prodotti.append(p)

    # metodo update: AGGIUNGETE VOI UNO O PIU` PARAMETRI AL POSTO DEI PUNTINI
    def update(self, prodotto, tipo_azione):
        if tipo_azione == "V":
            print("\nNuova vendita del prodotto {0}: quantita` disponibile = {1}".format(prodotto.nome,
                                                                                         prodotto.quantita))
            if prodotto.quantita < prodotto.MAXSCORTE / 3:
                print("Necessario approvvigionamento del prodotto {}".format(prodotto.nome))
                prodotto.immagazzina(prodotto.MAXSCORTE - prodotto.quantita)
        elif tipo_azione == "IM":
            print(
                "Immagazzinata una nuova quantita` del prodotto {0}: quantita` disponibile = {1}".format(prodotto.nome,
                                                                                                         prodotto.quantita))
        elif tipo_azione == "N":
            print("Nuovo acquirente del prodotto {0}".format(prodotto.nome))
        elif tipo_azione == "S":
            print("Cambio dello stato delle scorte del prodotto {0}: il prodotto ora e` nello stato {1}".format(
                prodotto.nome, prodotto.stato_scorte))


class StoricoGrossista:
    def __init__(self):
        self.storico = []

    # metodo update: AGGIUNGETE VOI UNO O PIU` PARAMETRI AL POSTO DEI PUNTINI
    def update(self, prodotto, tipo_azione):
        if tipo_azione == "V":
            self.storico.append("\ngiorno {0}: vendita del prodotto {1}".format(date.today(),prodotto.nome))
        elif tipo_azione == "IM":
            self.storico.append("\ngiorno {0}: immagazzinamento di una nuova quantita` del prodotto {1}".format(date.today(),prodotto.nome))
        elif tipo_azione == "S":
            self.storico.append("c'e` stato un cambio stato delle scorte del prodotto: il nuovo stato e` {0}".format(prodotto.stato_scorte));
        elif tipo_azione == "N":
            self.storico.append("La vendita e` effettuata ad un nuovo acquirente")

    def stampa_report(self):
        o = open("Report.txt", "a")
        for s in self.storico:
            o.write(s + "\n")
        o.close()


def main():
    p1 = ProdottoOsservato("Paperini")
    p2 = ProdottoOsservato("Nuterra")

    print("Inizialmente il prodotto {} e` nello stato {}".format(p1.nome, p1.stato_scorte))
    print("Inizialmente il prodotto {} e` nello stato {}\n".format(p2.nome, p2.stato_scorte))

    g = Grossista("GrossistaCampania", [p1, p2])
    gs = StoricoGrossista()
    p1.stato_scorte = 1000

    for p in g.prodotti:
        p.observers_add(g, gs)
        p.immagazzina(ProdottoOsservato.MAXSCORTE)

    c = 0
    for p in g.prodotti:
        p.vendi("SupermarketSun", 310 + c)
        p.vendi("SupermarketLongS", 300 + c)
        p.vendi("SupermarketFoop", 160 + c)
        p.vendi("SupermarketPrai", 305 + c)
        p.vendi("SupermarketLongS", 330 + c)
        c += 10

    print("\n\nCreo un report")
    gs.stampa_report()


if __name__ == "__main__":
    main()

"""Il programma deve stampare:
Inizialmente il prodotto Paperini e` nello stato non disponibile
Inizialmente il prodotto Nuterra e` nello stato non disponibile

Immagazzinata una nuova quantita` del prodotto Paperini: quantita` disponibile = 1000
Cambio dello stato delle scorte del prodotto Paperini: il prodotto ora e` nello stato altamente disponibile
Immagazzinata una nuova quantita` del prodotto Nuterra: quantita` disponibile = 1000
Cambio dello stato delle scorte del prodotto Nuterra: il prodotto ora e` nello stato altamente disponibile

Nuova vendita del prodotto Paperini: quantita` disponibile = 690
Nuovo acquirente del prodotto Paperini
Cambio dello stato delle scorte del prodotto Paperini: il prodotto ora e` nello stato disponibile

Nuova vendita del prodotto Paperini: quantita` disponibile = 390
Nuovo acquirente del prodotto Paperini

Nuova vendita del prodotto Paperini: quantita` disponibile = 230
Necessario approvvigionamento del prodotto Paperini
Immagazzinata una nuova quantita` del prodotto Paperini: quantita` disponibile = 1000
Cambio dello stato delle scorte del prodotto Paperini: il prodotto ora e` nello stato altamente disponibile
Nuovo acquirente del prodotto Paperini

Nuova vendita del prodotto Paperini: quantita` disponibile = 695
Nuovo acquirente del prodotto Paperini
Cambio dello stato delle scorte del prodotto Paperini: il prodotto ora e` nello stato disponibile

Nuova vendita del prodotto Paperini: quantita` disponibile = 365

Nuova vendita del prodotto Nuterra: quantita` disponibile = 680
Nuovo acquirente del prodotto Nuterra
Cambio dello stato delle scorte del prodotto Nuterra: il prodotto ora e` nello stato disponibile

Nuova vendita del prodotto Nuterra: quantita` disponibile = 370
Nuovo acquirente del prodotto Nuterra

Nuova vendita del prodotto Nuterra: quantita` disponibile = 200
Necessario approvvigionamento del prodotto Nuterra
Immagazzinata una nuova quantita` del prodotto Nuterra: quantita` disponibile = 1000
Cambio dello stato delle scorte del prodotto Nuterra: il prodotto ora e` nello stato altamente disponibile
Nuovo acquirente del prodotto Nuterra

Nuova vendita del prodotto Nuterra: quantita` disponibile = 685
Nuovo acquirente del prodotto Nuterra
Cambio dello stato delle scorte del prodotto Nuterra: il prodotto ora e` nello stato disponibile

Nuova vendita del prodotto Nuterra: quantita` disponibile = 345


Creo un report
"""

"""Il file Report contiene:

giorno 2019-12-16: immagazzinamento di una nuova quantita` del prodotto Paperini
c'e` stato  un cambio stato delle scorte del prodotto: il nuovo stato e` altamente disponibile

giorno 2019-12-16: immagazzinamento di una nuova quantita` del prodotto Nuterra
c'e` stato  un cambio stato delle scorte del prodotto: il nuovo stato e` altamente disponibile

giorno 2019-12-16: vendita del prodotto Paperini
La vendita e` effettuata ad un nuovo acquirente
c'e` stato  un cambio stato delle scorte del prodotto: il nuovo stato e` disponibile

giorno 2019-12-16: vendita del prodotto Paperini
La vendita e` effettuata ad un nuovo acquirente

giorno 2019-12-16: vendita del prodotto Paperini

giorno 2019-12-16: immagazzinamento di una nuova quantita` del prodotto Paperini
c'e` stato  un cambio stato delle scorte del prodotto: il nuovo stato e` altamente disponibile
La vendita e` effettuata ad un nuovo acquirente

giorno 2019-12-16: vendita del prodotto Paperini
La vendita e` effettuata ad un nuovo acquirente
c'e` stato  un cambio stato delle scorte del prodotto: il nuovo stato e` disponibile

giorno 2019-12-16: vendita del prodotto Paperini

giorno 2019-12-16: vendita del prodotto Nuterra
La vendita e` effettuata ad un nuovo acquirente
c'e` stato  un cambio stato delle scorte del prodotto: il nuovo stato e` disponibile

giorno 2019-12-16: vendita del prodotto Nuterra
La vendita e` effettuata ad un nuovo acquirente

giorno 2019-12-16: vendita del prodotto Nuterra

giorno 2019-12-16: immagazzinamento di una nuova quantita` del prodotto Nuterra
c'e` stato  un cambio stato delle scorte del prodotto: il nuovo stato e` altamente disponibile
La vendita e` effettuata ad un nuovo acquirente

giorno 2019-12-16: vendita del prodotto Nuterra
La vendita e` effettuata ad un nuovo acquirente
c'e` stato  un cambio stato delle scorte del prodotto: il nuovo stato e` disponibile

giorno 2019-12-16: vendita del prodotto Nuterra
"""
