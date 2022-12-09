from mod import Cane, Persona, Mediator
import datetime


# completare la classe Casa (completare  __init__ e aggiungere i metodi necessari)
class Casa:

    def caneAbbaiato(self,widget):
        self.allerta = True

    def ControlloCani(self,widget):
        if self.allerta:
            differenza1 = self.padrone.ora_ritorno - self.cane1.oraUltimaPappa
            differenza2 = self.padrone.ora_ritorno - self.cane2.oraUltimaPappa

            if differenza1.seconds > 14400:
                print("il padrone da' da mangiare al cane " + self.cane1.nome)
                self.cane1.oraUltimaPappa = self.padrone.ora_ritorno
            if differenza2.seconds > 14400:
                print("il padrone da' da mangiare al cane " + self.cane2.nome)
                self.cane2.oraUltimaPappa = self.padrone.ora_ritorno
            self.allerta = False

    def __init__(self, nomePadrone, nomeCane1, nomeCane2, oraUltimaPappa1, oraUltimaPappa2):
        self.allerta = False
        self.padrone = Persona(nomePadrone)
        self.cane1 = Cane(nomeCane1, oraUltimaPappa1)
        self.cane2 = Cane(nomeCane2, oraUltimaPappa2)
        self.mediator = Mediator(((self.padrone, self.ControlloCani), (self.cane1,self.caneAbbaiato),(self.cane2,self.caneAbbaiato)))


def main():
    casa = Casa("Maria", "Bob", "Ted", datetime.datetime(year=2020, month=1, day=11, hour=10),
                datetime.datetime(year=2020, month=1, day=11, hour=11))
    print("Il cane {} ha mangiato alle {} per l'ultima volta".format(casa.cane1.nome,
                                                                     (casa.cane1.oraUltimaPappa.strftime('%H:%M'))))
    print("Il cane {} ha mangiato alle {} per l'ultima volta".format(casa.cane2.nome,
                                                                     (casa.cane2.oraUltimaPappa.strftime('%H:%M'))))

    casa.padrone.esce()
    casa.cane1.abbaia()
    casa.padrone.torna_a_casa(datetime.datetime(year=2020, month=1, day=11, hour=15))
    casa.padrone.esce()
    casa.cane2.abbaia()
    casa.padrone.torna_a_casa(datetime.datetime(year=2020, month=1, day=11, hour=17))
    casa.padrone.esce()
    casa.padrone.torna_a_casa(datetime.datetime(year=2020, month=1, day=11, hour=18))
    casa.padrone.esce()
    casa.cane1.abbaia()
    casa.padrone.torna_a_casa(datetime.datetime(year=2020, month=1, day=11, hour=23))


if __name__ == "__main__": main()

"""
Il programma deve stampare:
Il cane Bob ha mangiato alle 10:00 per l'ultima volta
Il cane Ted ha mangiato alle 11:00 per l'ultima volta
Il padrone dei cani esce di casa
Il cane Bob abbaia
Il padrone dei cani torna a casa alle 15:00
Il padrone da` la pappa al cane  Bob
Il padrone dei cani esce di casa
Il cane Ted abbaia
Il padrone dei cani torna a casa alle 17:00
Il padrone da` la pappa al cane  Ted
Il padrone dei cani esce di casa
Il padrone dei cani torna a casa alle 18:00
Il padrone dei cani esce di casa
Il cane Bob abbaia
Il padrone dei cani torna a casa alle 23:00
Il padrone da` la pappa al cane  Bob
Il padrone da` la pappa al cane  Ted


"""
