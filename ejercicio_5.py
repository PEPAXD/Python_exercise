#PYTHON
#Crear un conversor entre varias unidades monetarias, que el usuario pueda elegir la opcion a convertir

#LIBRERIAS
import sys

#Variables  ---- > ACTUALIZAR LAS VARIABLES ANTES DE EJECUTAR
dolar_usd = 1.0
peso_ars = 110.91
real_brasileno = 4.74
euro = 0.91
yen = 122.09

#TITULO
texto1 = "CONVERSOR DE UNIDADES"
texto2 = "SELECCIONE SU MONEDA DE CAMBIO: "
print("\n"+ texto1 +"\n"+"-"*len(texto2))

#CAMBIO MONEDAS
print("INDIQUE LA MONEDA QUE POSEE")
moneda_a = int(input("1) USD"+"\n"+"2) ARS" +"\n"+ "3) BRL" +"\n"+ "4) EUR" +"\n"+ "5) YEN" + "\n"+"-"*len(texto2)+"\n"+ "OPCION: "))

if(moneda_a == 1):
    moneda_fija = dolar_usd
    moneda_a_text = "USD"
elif(moneda_a == 2):
    moneda_fija = peso_ars
    moneda_a_text = "ARS"
elif(moneda_a == 3):
    moneda_fija = real_brasileno
    moneda_a_text = "BRL"
elif(moneda_a == 4):
    moneda_fija = euro
    moneda_a_text = "EUR"
elif(moneda_a == 5 ):
    moneda_fija = yen
    moneda_a_text = "YEN"
else:
    sys.exit("\nSOLO SE ADMITEN LOS VALORES 1,2,3,4 o 5 \nFINALIZANDO PROCESO")

#CANTIDAD A CAMBIAR
dinero_total = float(input("-"*len(texto2)+"\n" + "CUANTO DINERO DESEA CAMBIAR: "))

#MONEDA DE CAMBIO
print("-"*len(texto2)+"\n"+"SELECCIONE SU MONEDA DE CAMBIO: ")

#CAMBIO MONEDAS
moneda_b = int(input("1) USD"+"\n"+"2) ARS" +"\n"+ "3) BRL" +"\n"+ "4) EUR" +"\n"+ "5) YEN" + "\n"+"-"*len(texto2)+"\n"+ "OPCION: "))
print("-"*len(texto2))

if(moneda_b == 1):
    moneda_cambio = dolar_usd
    moneda_b_text = "USD"
elif(moneda_b == 2):
    moneda_cambio = peso_ars
    moneda_b_text = "ARS"
elif(moneda_b == 3):
    moneda_cambio = real_brasileno
    moneda_b_text = "BRL"
elif(moneda_b == 4):
    moneda_cambio = euro
    moneda_b_text = "EUR"
elif(moneda_b == 5 ):
    moneda_cambio = yen
    moneda_b_text = "YEN"
else:
    sys.exit("\nSOLO SE ADMITEN LOS VALORES 1,2,3,4 o 5 \nFINALIZANDO PROCESO")

#CONVERSION
conversion_resultado = (dinero_total * moneda_cambio)/moneda_fija

#IMPRIMO RESULTADO FINAL
print("{0:.2f} ".format(dinero_total) + moneda_a_text + " ---> " + "{0:.2f} ".format(conversion_resultado) + moneda_b_text)
