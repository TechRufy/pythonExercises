
class Utente(): 

    def __init__(self,nome,cognome,matricola):
        self.nome = nome
        self.cognome = cognome
        self.matricola = matricola

   
    def __str__(self):
        return self.nome + " " + self.cognome + " " + str(self.matricola)
