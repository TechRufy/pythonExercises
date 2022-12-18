import collections
import multiprocessing


def conteggioEstampa(jobs, ListaParole):
    conteggio = collections.defaultdict()

    while True:
        for parole in ListaParole:
            conteggio[parole] = 0
        try:
            file = jobs.get()

            f = open(file, "r")

            for line in f:
                paroleLinea = line.split(" ")
                for parola in paroleLinea:
                    if parola in ListaParole:
                        conteggio[parola] += 1

            max = 0
            parolamigliore = ""
            for parola, num in conteggio.items():
                if num >= max:
                    parolamigliore = parola
                    max = num


        finally:
            jobs.task_done()
        print("La stringa della lista ['computer', 'very', 'with', 'is', 'algorithms'] "
              "che appare il maggior numero di volte nel file {0} e` {1}. Essa appare {2} volte nel file.".format(file,parolamigliore,conteggio[parolamigliore]))


def stampaParole(ListaFile, ListaParole, numConcorrenza):
    coda = multiprocessing.JoinableQueue()

    for _ in range(numConcorrenza):
        process = multiprocessing.Process(target=conteggioEstampa, args=(coda, ListaParole))
        process.daemon = True
        process.start()

    for file in ListaFile:
        coda.put(file)

    try:
        coda.join()
    except KeyboardInterrupt:
        print("interrotto")


def main():
    files = ["file1", "file2", "file3", "file4"]
    parole = ["computer", "very", "with", "is", "algorithms"]

    stampaParole(files, parole, 2)


if __name__ == "__main__":
    main()

"""  Ecco cosa deve essere stampato (l'ordine delle righe potrebbe cambiare):
La stringa della lista ['computer', 'very', 'with', 'is', 'algorithms'] che appare il maggior numero di volte nel file file2 e` "very".
Essa appare 3 volte nel file.

La stringa della lista ['computer', 'very', 'with', 'is', 'algorithms'] che appare il maggior numero di volte nel file file1 e` "computer".
Essa appare 48 volte nel file.

La stringa della lista ['computer', 'very', 'with', 'is', 'algorithms'] che appare il maggior numero di volte nel file file4 e` "is".
Essa appare 2 volte nel file.

La stringa della lista ['computer', 'very', 'with', 'is', 'algorithms'] che appare il maggior numero di volte nel file file3 e` "is".
Essa appare 113 volte nel file.

"""
