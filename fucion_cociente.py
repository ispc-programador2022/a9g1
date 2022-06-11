#Funsión Cociente
#Retorna el cociente entre 2 parámetros.



val1=int(input("Por favor, ingrese el primer número que desea dividir: "))
val2=int(input("Por favor, ingrese el segundo número por el cual dividir: "))



def cociente(x, y):
    return x / y


print("El resultado de su operación es: ",int(cociente(val1, val2)))