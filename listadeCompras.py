#HACER UNA LISTA DE COMPRA, EL PROGRAMA PREGUNTA AL USUARIO INGREDIENTES PARA AGREGAR

#EJEMPLO 1: QUE DESEA COMPRAR? ([Q TO EXIT) > leche
#         ESTA SEGURO QUE DESEA AGREGAR "leche" A LA LISTA? [Y/N]: > Y
#         Leche se ha añadido a la lista!!!

#EJEMPLO 2: QUE DESEA COMPRAR? ([Q TO EXIT) > PAN
#         Pan se ha añadido a la lista!!!
#           QUE DESEA COMPRAR? ([Q TO EXIT) > PAN
#         pan ya estaba en la lista... ingrese otro ingrediente

#EJEMPLO 3: QUE DESEA COMPRAR? ([Q TO EXIT) > Q
#         [MOSTRAR LISTA DE COMPRA] > LOS INGREDIENTES A COMPRAR SON: 1) LECHE, 2) PAN, 3) TOMATES, etc...

#LIBRERIAS
import os

#VARIABLES
lista_compra = []
long_text = "------------------------------------------------------------------------"
ingrediente = None
numero_ingrediente  = 1

#COLOR
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

#CREDITOS AL PROGRAMADOR
print(RED+"\nSHOP LIST BY MAURO PEPA. V1.0"+RESET)

while ingrediente != "x":

    # TEXT
    print("-" * len(long_text))
    print(BLUE + "Que desea comprar? [PRESS X TO EXIT]\n")
    ingrediente = input("AÑADIR A MI LISTA: " + RESET)

    #ANTI-REPEAT INGREDIENT
    while ingrediente in lista_compra:
        ingrediente = input("-" * len(long_text)+"\n"+RED+ingrediente+" ya estaba en la lista... ingrese otro ingrediente: "+RESET)

    #CERRAR LISTA
    if(ingrediente!="x"):

        # CONFIRMACION ADDLIST
        print("\nESTA SEGURO DE QUE DESEA AGREGAR [" + ingrediente + "] A LA LISTA?")
        confirmar_addlist = input("OPCION [Y/N]: ")

        if (confirmar_addlist == "y"):

            # ADD LIST
            lista_compra.append(ingrediente)
            print("-" * len(long_text)+"\n"+MAGENTA + ingrediente + " se ha añadido a la lista!!!" + RESET)

    # BORRAS TEXTO CONSOLA
    # os.system("cls")

#MOSTRAR LISTA
print("-" * len(long_text)+"\n"+YELLOW+"LOS INGREDIENTES A COMPRAR SON:\n")

#TAMAÑO LIST
while numero_ingrediente <= len(lista_compra):

    print("{}) ".format(numero_ingrediente)+lista_compra[numero_ingrediente-1])
    numero_ingrediente += 1

print(RESET+"-" * len(long_text))