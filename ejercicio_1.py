# crear un programa en el cual el usuario introduzca 3 numeros y devuelva el valor mas grande y el mas pequeño

#USUARIO INGRESA 3 VARIABLES
a = int(input("INGRESE UN VALOR PARA (A) = "))
b = int(input("INGRESE UN VALOR PARA (B) = "))
c = int(input("INGRESE UN VALOR PARA (C) = "))

#VALOR MAX
ValorMax = str(max(a, b, c))

#VALOR MIN
ValorMin = str(min(a, b, c))

#IMPRIMO RESULTADOS
print()
print("EL VALOR MAS GRANDE ES: "+ValorMax)
print("EL VALOR MAS PEQUEÑO ES: "+ValorMin)



