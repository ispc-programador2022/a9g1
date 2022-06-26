import primer_tp
import funcion_resta

print ("""          BIENVENIDOS 
           Somos el grupo 1 del Aula 9   """)

def ing2i ():
    val1=int(input("Por favor, ingrese el primer número : "))
    val2=int(input("Por favor, ingrese el segundo número : "))
    return [val1,val2]

option = 0;

while option != 31 :
    print ("""  Ingrese la opcion que desea 
            1- Funcion suma
            2- funcion resta 
            3- funcion producto
            4- Funcion cociente 
            31- Salir""")
    option = int(input("ingrese el su opcion : "))
    if option == 1:
        varList = ing2i()
        result = primer_tp.suma(varList[0],varList[1])
        print (" El resultado de la suma es : " , result)
    elif option == 2 :
        varList = ing2i()
        result = funcion_resta.resta(varList[0],varList[1])
        print (" El resultado de la resta es : " , result)
    elif option == 31 :
        print(" Muchas gracias")
    else :
        print("Opcion incorrecta. ")