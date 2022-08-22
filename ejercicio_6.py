#CREAR UN PROGRAMA PARA AYUDAR A UN USUARIO EN LA COMPRA DE UN CELULAR

#LIBRERIAS
import sys

#SISTEMA OPERATIVO
texto_1_long = "Que sistema operativo desea?"
print("\n" + "Que sistema operativo desea?"+"\n"+"-"*len(texto_1_long))
print("1) IOS"+ "\n" + "2) ANDROID" +"\n"+"-"*len(texto_1_long))

sistema_operativo = int(input("OPCION: "))
print("-"*len(texto_1_long))

#ANDROID
if(sistema_operativo == 2):
    print(("1) GAMA ALTA"+ "\n" + "2) GAMA BAJA"+"\n"+"-"*len(texto_1_long)))
    gama = int(input("OPCION: "))
    print("-"*len(texto_1_long))

    #GAMA ALTA/BAJA
    if(gama == 2):
        print("ANDROID CHINO USD $100")
        exit()


    elif(gama == 1):
        print(("1) CAMARA ALTA RESOLUCION"+ "\n" + "2) CAMARA BAJA RESOLUCION"+"\n"+"-"*len(texto_1_long)))
        camara = int(input("OPCION: "))
        print("-" * len(texto_1_long))

    #CAMARA ALTA/BAJA
        if(camara == 2):
            print("ANDROID CLASICO USD $300")
            exit()

        elif (camara == 1):
            print("ANDROID PROFESIONAL USD $500")
            exit()

#IOS
elif(sistema_operativo == 1):
    print(("1) GAMA ALTA" + "\n" + "2) GAMA BAJA" + "\n" + "-" * len(texto_1_long)))
    gama = int(input("OPCION: "))
    print("-" * len(texto_1_long))

    #GAMA ALTA/BAJA
    if (gama == 2):
        print("IOS IMITACION USD $200")
        exit()

    elif (gama == 1):
        print(("1) CAMARA ALTA RESOLUCION" + "\n" + "2) CAMARA BAJA RESOLUCION" + "\n" + "-" * len(texto_1_long)))
        camara = int(input("OPCION: "))
        print("-" * len(texto_1_long))

        # CAMARA ALTA/BAJA
        if (camara == 2):
            print("IOS CLASICO USD $600")
            exit()

        elif (camara == 1):
            print("IOS PROFESIONAL USD $1000")
            exit()

else:
    sys.exit("\nSOLO SE ADMITEN LOS VALORES 1 o 2\nFINALIZANDO PROCESO!!!")