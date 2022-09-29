import math
import os
import django

posizione = dir(math).index("tan")
funzione = dir(math).pop(posizione)

print(funzione)

funzione_2 = None

for nome in dir(math):
    if nome == "tan":
        funzione_2 = nome


print(funzione_2)



