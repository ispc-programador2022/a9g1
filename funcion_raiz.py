# Función Radicación
# Retorna la raiz del primero respecto del segundo parámetros.


val1=int(input("Por favor, ingrese el número que desea sacar la raíz cuadrada "))
val2=int(input("Por favor, ingrese el número de la raiz: "))



def raiz(x, y):
    return x // y


print("El resultado de su operación es: ",float(raiz(val1, val2)))