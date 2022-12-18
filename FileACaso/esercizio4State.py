# altro esempio di concorrenza
import sys
import multiprocessing

from datetime import date


def processaProdotti(prodotti, liste_acquirenti, concorrenza):
    jobs = multiprocessing.JoinableQueue()
    for _ in range(concorrenza):
        process = multiprocessing.Process(target=Worker,args=((jobs,)))
        process.daemon=True
        process.start()
    for prodotto, lista in zip(prodotti, liste_acquirenti):
        jobs.put((prodotto, lista))

    try:
        jobs.join()
    except KeyboardInterrupt:
        print("interrotto")

def Worker(jobs):
    while True:
        prodotto, acquirenti = jobs.get()
        try:
            for acquirente in acquirenti:
                prodotto.aggiorna(*acquirente)

        finally:
            print("il dizionario del prodotto {0} contiene {1} entrate".format(prodotto.nome,len(prodotto.acquirenti)))
            for nome,valore in prodotto.acquirenti.items():
                print(nome,*valore)
            jobs.task_done()


class ProdottoSemplice():

    def __init__(self, nome):
        self.nome = nome

        self.acquirenti = dict()

    def aggiorna(self, nome, numero, data):
        self.acquirenti[nome] = (numero, data)


def main():
    p1 = ProdottoSemplice("Paperini")
    p2 = ProdottoSemplice("Nuterra")
    p3 = ProdottoSemplice("Totatola")
    p4 = ProdottoSemplice("Dask")
    p5 = ProdottoSemplice("Duondidolla")

    p1.aggiorna("SupermarketSun", 310, date(2019, 10, 30))
    p1.aggiorna("SupermarketLongS", 300, date(2018, 11, 24))
    p2.aggiorna("SupermarketLongS", 200, date(2019, 6, 11))
    p5.aggiorna("SupermarketSun", 500, date(2016, 2, 10))
    prodotti = [p1, p2, p3, p4, p5]
    l1 = [("SupermarketLongS", 100, date.today())]
    s = 25
    for c in range(ord('a'), ord('p')):
        l1.append(("SupermarketLong" + chr(c), s, date.today()))
        s += 10
    l2 = []
    s = 30
    for c in range(ord('A'), ord('Y')):
        l2.append(("SupermarketLong" + chr(c), s, date.today()))
        s += 10
    l2.append(("SupermarketLongS", 65, date.today()))

    l3 = []
    s = 33
    for c in range(ord('A'), ord('W')):
        l3.append(("SupermarketLong" + chr(c), s, date.today()))
        s += 10
    l4 = []
    s = 11
    for c in range(ord('M'), ord('X')):
        l4.append(("SupermarketLong" + chr(c), s, date.today()))
        s += 10
    l5 = []
    s = 39
    for c in range(ord('F'), ord('Q')):
        l5.append(("SupermarketLong" + chr(c), s, date.today()))
        s += 10
    l5.append(("SupermarketSun", 20, date.today()))

    liste_acquirenti = [l1, l2, l3, l4, l5]
    # potete modificare l'ultimo arogmento
    processaProdotti(prodotti, liste_acquirenti, 5)


if __name__ == "__main__":
    main()

"""Il programma deve stampare (l'ordine in cui vengono stampate le informazioni relative a ciscun prodotto puo` cambiare):

Il dizionario acquirenti del prodotto Paperini contiene 17 entrate dopo i nuovi inserimenti.
Le entrate del dizionario aggiornato contengono:
SupermarketSun 310 2019-10-30
SupermarketLongS 100 2019-12-16
SupermarketLonga 25 2019-12-16
SupermarketLongb 35 2019-12-16
SupermarketLongc 45 2019-12-16
SupermarketLongd 55 2019-12-16
SupermarketLonge 65 2019-12-16
SupermarketLongf 75 2019-12-16
SupermarketLongg 85 2019-12-16
SupermarketLongh 95 2019-12-16
SupermarketLongi 105 2019-12-16
SupermarketLongj 115 2019-12-16
SupermarketLongk 125 2019-12-16
SupermarketLongl 135 2019-12-16
SupermarketLongm 145 2019-12-16
SupermarketLongn 155 2019-12-16
SupermarketLongo 165 2019-12-16

Il dizionario acquirenti del prodotto Nuterra contiene 24 entrate dopo i nuovi inserimenti.
Le entrate del dizionario aggiornato contengono:
SupermarketLongS 65 2019-12-16
SupermarketLongA 30 2019-12-16
SupermarketLongB 40 2019-12-16
SupermarketLongC 50 2019-12-16
SupermarketLongD 60 2019-12-16
SupermarketLongE 70 2019-12-16
SupermarketLongF 80 2019-12-16
SupermarketLongG 90 2019-12-16
SupermarketLongH 100 2019-12-16
SupermarketLongI 110 2019-12-16
SupermarketLongJ 120 2019-12-16
SupermarketLongK 130 2019-12-16
SupermarketLongL 140 2019-12-16
SupermarketLongM 150 2019-12-16
SupermarketLongN 160 2019-12-16
SupermarketLongO 170 2019-12-16
SupermarketLongP 180 2019-12-16
SupermarketLongQ 190 2019-12-16
SupermarketLongR 200 2019-12-16
SupermarketLongT 220 2019-12-16
SupermarketLongU 230 2019-12-16
SupermarketLongV 240 2019-12-16
SupermarketLongW 250 2019-12-16
SupermarketLongX 260 2019-12-16

Il dizionario acquirenti del prodotto Dask contiene 11 entrate dopo i nuovi inserimenti.
Le entrate del dizionario aggiornato contengono:
SupermarketLongM 11 2019-12-16
SupermarketLongN 21 2019-12-16
SupermarketLongO 31 2019-12-16
SupermarketLongP 41 2019-12-16
SupermarketLongQ 51 2019-12-16
SupermarketLongR 61 2019-12-16
SupermarketLongS 71 2019-12-16
SupermarketLongT 81 2019-12-16
SupermarketLongU 91 2019-12-16
SupermarketLongV 101 2019-12-16
SupermarketLongW 111 2019-12-16

Il dizionario acquirenti del prodotto Duondidolla contiene 12 entrate dopo i nuovi inserimenti.
Le entrate del dizionario aggiornato contengono:
SupermarketSun 20 2019-12-16
SupermarketLongF 39 2019-12-16
SupermarketLongG 49 2019-12-16
SupermarketLongH 59 2019-12-16
SupermarketLongI 69 2019-12-16
SupermarketLongJ 79 2019-12-16
SupermarketLongK 89 2019-12-16
SupermarketLongL 99 2019-12-16
SupermarketLongM 109 2019-12-16
SupermarketLongN 119 2019-12-16
SupermarketLongO 129 2019-12-16
SupermarketLongP 139 2019-12-16

Il dizionario acquirenti del prodotto Totatola contiene 22 entrate dopo i nuovi inserimenti.
Le entrate del dizionario aggiornato contengono:
SupermarketLongA 33 2019-12-16
SupermarketLongB 43 2019-12-16
SupermarketLongC 53 2019-12-16
SupermarketLongD 63 2019-12-16
SupermarketLongE 73 2019-12-16
SupermarketLongF 83 2019-12-16
SupermarketLongG 93 2019-12-16
SupermarketLongH 103 2019-12-16
SupermarketLongI 113 2019-12-16
SupermarketLongJ 123 2019-12-16
SupermarketLongK 133 2019-12-16
SupermarketLongL 143 2019-12-16
SupermarketLongM 153 2019-12-16
SupermarketLongN 163 2019-12-16
SupermarketLongO 173 2019-12-16
SupermarketLongP 183 2019-12-16
SupermarketLongQ 193 2019-12-16
SupermarketLongR 203 2019-12-16
SupermarketLongS 213 2019-12-16
SupermarketLongT 223 2019-12-16
SupermarketLongU 233 2019-12-16
SupermarketLongV 243 2019-12-16


"""
