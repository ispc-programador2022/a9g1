# Función Potencia
# Retorna la potencia del primero elevado al segundo parámetros.


val1=int(input("Por favor, ingrese el número que desea potenciarlo: "))
val2=int(input("Por favor, ingrese el número por el cual desea elevar el primer valor: "))



def potencia(x, y):
    return x ** y


print("El resultado de su operación es:",int(potencia(val1, val2)))