import random
import pandas as pd
from itertools import combinations

def genrnd ():
    lista_50 = []
    for x in range (50):
        numeros_aleatorios = random.randint(0, 100)
        lista_50.append(numeros_aleatorios)
    return lista_50


lista_aleatoria = genrnd()

print(lista_aleatoria)

temp = combinations(lista_aleatoria, 2)
for i in list(temp):
	print (i[0], '+', i[1], '=', sum(i))




"""

def sumgenr():
lista= genrnd()
total= 0
for i in range(0,len(lista)+1):
    for j in range(0,len(lista)):
        total= lista[i] + lista[j]
        return total


"""


