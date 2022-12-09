import collections
import copy
import itertools
import datetime
import time


class Observed:
    def __init__(self):
        self.__observers = set()

    def observers_add(self, observer, *observers):
        for observer in itertools.chain((observer,), observers):
            self.__observers.add(observer)
            observer.update(self)

    def observer_discard(self, observer):
        self.__observers.discard(observer)

    def observers_notify(self):
        for observer in self.__observers:
            observer.update(self)


class LaureaT_Student(Observed):

    def __init__(self, cfu):
        super().__init__()
        self.total_cfu = cfu
        self.__english_r = False
        self.grades = collections.defaultdict(int)

    @property
    def english_r(self):
        return self.__english_r

    @english_r.setter
    def english_r(self, english_r):
        if self.__english_r != english_r:
            self.__english_r = english_r
            self.observers_notify()

    def add_grade(self, Esame, voto):
        self.grades[Esame[0]] = voto
        self.total_cfu = self.total_cfu + Esame.cfu
        self.observers_notify()


class HistoryView:

    def __init__(self):
        self.data = []

    def update(self, studente):
        self.data.append((copy.copy(studente.grades), studente.english_r, time.time()))


class LiveView:

    def __init__(self):
        self.statoPrecedente = None

    def update(self, studente):
        if self.statoPrecedente is None:
            if studente.english_r:
                print("Cambio stato: lo studente ha appena superato la prova di Inglese\n")
            elif studente.total_cfu != 0:
                print("Cambio stato: lo studente ha superato un nuovo esame")
                print("Cambio stato: il numero di CFU e` : ", studente.total_cfu, "\n")
            self.statoPrecedente = studente.english_r
        else:
            if self.statoPrecedente != studente.english_r:
                print("Cambio stato: lo studente ha appena superato la prova di Inglese\n")
            else:
                print("Cambio stato: lo studente ha superato un nuovo esame")
                print("Cambio stato: il numero di CFU e` : ", studente.total_cfu, "\n")
            self.statoPrecedente = studente.english_r


Exam = collections.namedtuple("Exam", "name cfu")


def main():
    historyView = HistoryView()
    liveView = LiveView()
    student = LaureaT_Student(0)
    student.observers_add(historyView, liveView)

    print("Lo studente sta per superare analisi matematica")
    student.add_grade(Exam("analisi matematica", 9), 28)
    print("Lo studente sta per superare asistemi operativi")
    student.add_grade(Exam("sistemi operativi", 6), 20)
    print("Lo studente sta per superare la prova di Inglese")
    student.english_r = True

    for grades, flag, timestamp in historyView.data:
        print("Esami: {}, Inglese: {}, Data: {}".format([(key, value) for key, value in grades.items()],
                                                        " " if flag == None else "superato" if flag else "non superato",
                                                        datetime.datetime.fromtimestamp(timestamp)))


if __name__ == "__main__": main()
