import random
import statistics

def genrnd ():
    lista_50 = []
    for x in range (50):
        numeros_aleatorios = random.randint(0, 100)
        lista_50.append(numeros_aleatorios)
    return lista_50

print("Lista de 50 numeros aleatorios: ",genrnd())

data = genrnd()
mediana = statistics.median(data) 

print("La mediana es: ", mediana)