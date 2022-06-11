#Funsión Módulo
#Retorna el módulo entre 2 parámetros.



val1=int(input("Por favor, ingrese el primer número que desea dividir: "))
val2=int(input("Por favor, ingrese el segundo número por el cual dividir: "))



def modulo(x, y):
    return x % y


print("El módulo de su operación es:",float(modulo(val1, val2)))