#El usuario debe adivinar un numero entre el 1 al 10
# Si es verdadero se felicita al usuario si es falso finaliza el programa

#LIBRERIAS
import random
import sys

#VARIABLE RANDOM
NumY = random.randint(1, 10)

#USUARIO INGRESA UN NUMERO
NumX = int(input("INGRESE UN NUMERO ENTRE 1 y 10: "))

if(NumX < 1 or NumX > 10 ):
    sys.exit("\nEL VALOR INGRESADO NO CUMPLE CON LA CONSIGNA ANTERIOR... \nFINALIZANDO PROCESO")

#PREGUNTO SI EL RESULTADO COINCIDE
if(NumX==NumY):
    print("\nFELICIDADES EL NUMERO INGRESADO ES CORRECTO!!!")
if(NumX!=NumY):
    print("\nEL NUMERO INGRESADO ES INCORRECTO, LA VARIABLE ALEATORIA ERA: ({})".format(NumY))

