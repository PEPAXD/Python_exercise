#TEST GAMER
#HACER UN TEST CON UNA SERIE DE PREGUNTAS, SUMAR PUNTOS TOTALES Y DEVOLVER UN RESULTADO AL USUARIO

#LIBRERIAS
import sys

#VARIABLES
texto1 = "Responde las preguntas y descubre qué tan gamer eres en realidad."
puntos_totales = 0

#TITULO
print("\n" + "TEST GAMER" + "\n" + "-"*len(texto1))

#TEXTO 1
print(texto1 + "\n" + "-"*len(texto1))

#PREGUNTA1
print("¿Qué significan las siglas GG\n")
print("A) Se usa al terminar una partida, aunque no se qué significa.")
print("B) Good Game o buen juego en español.")
print("C) Solo se que los freaks lo usan.")

print("-"*len(texto1))
pregunta_abc = input("OPCION: ")
print("-"*len(texto1))

#SUMAPUNTOS1
if(pregunta_abc == "a" or pregunta_abc == "A"):
    puntos_totales += 5
elif(pregunta_abc == "b" or pregunta_abc == "B"):
    puntos_totales += 10
elif(pregunta_abc == "c" or pregunta_abc == "C"):
    puntos_totales += 0
else:
    sys.exit("\nSOLO SE ADMITEN LOS VALORES A, B o C \nFINALIZANDO PROCESO")

#PREGUNTA2
print("¿cuantas horas semanales dedicas a los videojuegos?\n")
print("A) 1hs o menos")
print("B) 2 o 3 hs aproximadamente")
print("C) 6 hs o mas")

print("-"*len(texto1))
pregunta_abc = input("OPCION: ")
print("-"*len(texto1))

#SUMAPUNTOS2
if(pregunta_abc == "a" or pregunta_abc == "A"):
    puntos_totales += 0
elif(pregunta_abc == "b" or pregunta_abc == "B"):
    puntos_totales += 5
elif(pregunta_abc == "c" or pregunta_abc == "C"):
    puntos_totales += 10
else:
    sys.exit("\nSOLO SE ADMITEN LOS VALORES A, B o C \nFINALIZANDO PROCESO")

#PREGUNTA3
print("¿cuantos videojuegos jugaste en tu vida?\n")
print("A) 5 o menos")
print("B) entre 5 a 10 juegos aproximadamente")
print("C) mas de 10 seguro")

print("-"*len(texto1))
pregunta_abc = input("OPCION: ")
print("-"*len(texto1))

#SUMAPUNTOS3
if(pregunta_abc == "a" or pregunta_abc == "A"):
    puntos_totales += 0
elif(pregunta_abc == "b" or pregunta_abc == "B"):
    puntos_totales += 5
elif(pregunta_abc == "c" or pregunta_abc == "C"):
    puntos_totales += 10
else:
    sys.exit("\nSOLO SE ADMITEN LOS VALORES A, B o C \nFINALIZANDO PROCESO")

# SUMA TOTAL PUNTOS Y RESULTADO FINAL
if (puntos_totales < 15):
    print("RANGO GAMER (NOOB)" + "\n" + "-" * len(texto1))
elif(15 <= puntos_totales < 30):
    print("RANGO GAMER (CASUAL)" + "\n" + "-" * len(texto1))
elif(puntos_totales >= 30):
    print("RANGO GAMER (PROGAMER)" + "\n" + "-" * len(texto1))