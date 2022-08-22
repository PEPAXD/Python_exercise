#EJERCICIO N°1
#Conversor de grados farenheit a celcius / 45°F = 7°C / ((°F-32)*5/9 = °C)

#USUARIO INGRESA TEMPERATURA °F
TempF = int(input ("\nIngrese el valor de temperatura en °F: " ))

#CONVERSOR °F ---> °C
TempC = ((TempF-32) * 5/9)

#IMPRIMO RESULTADO
print("{}°F".format(TempF) + " ---> "+"{0:.1f}°C".format(TempC))   #.format convierte el valor de la unidad (int--->str)

#EJERCICIO N°2
#Conversor de Libras a Euros / 1L ---> 1,20E / Xl ---> Ye

#USUARIO INGRESA CANTIDAD DE LIBRAS A CONVERTIR
Libra = float(input ("\nIngrese el valor de libras a convertir: £" ))

#CONVERSOR °F ---> °C
Euro = ((Libra*1.20)/1)

#IMPRIMO RESULTADO
print("{}£".format(Libra) + " ---> "+"{0:.2f}€".format(Euro))