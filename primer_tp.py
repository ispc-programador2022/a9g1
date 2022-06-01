#ISPC: Curso Programación: Primer TP

# Crear un programa en Python que tendrá 3 o 4 funciones:
#  Suma, 3 parámetros, devuelve la suma de los 3.
#  Resta, 2 parámetros, devuelve la resta de los 2.
#  Producto, 4 parámetros, devuelve el producto de los 4.
#  Imprimir, 2 parámetros, texto y valor, devuelve la impresión de los valores pasados.
# Usaremos Visual Studio Code, con la extensión de Python para hacer la práctica.
# El equipo crea un Project en Githug y agrega 2 al menos 2 issue por cada tarea a realizar.
# Crear una rama por cada miembro.
# El primer integrante del grupo, creará el repositorio, creará un programa en Python con la función suma, y el main y subirá al repo el código producido

val1=int(input("Por favor, ingrese el primer número que desea sumar: "))
val2=int(input("Por favor, ingrese el segundo número que desea sumar: "))
val3=int(input("Por favor, ingrese el tercer número que desea sumar: "))



def suma (val1, val2, val3):
    return val1 + val2 + val3


print("La suma de sus números da el valor de: ",suma(val1, val2, val3))