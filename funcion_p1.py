# Función P1
# Retorna el producto de los 2 primero más el 3er parámetros, usando las funciones anteriores

val1=int(input("Por favor, ingrese el primer número que desea sumar: "))
val2=int(input("Por favor, ingrese el segundo número que desea sumar: "))
val3=int(input("Por favor, ingrese el tercer número que desea sumar a los dos anteriores: "))



def suma (x, y):
    return x + y

print("La suma de sus números da el valor de: ",suma(val1, val2) + val3)