#CREATE UN PROGRAMA QUE SEA CAPAZ DE DECIR EL NUMERO MAYOR Y EL MENOR DE UN ARREGLO
import numpy as np

x= input("Inserte la cantidad de números que se calculan: ")
cantidadNumeros= int(x)
numeros = np.arange(cantidadNumeros)



for numero in numeros:

    numeros[numero]= int(input("Inserte el número : "))


orden = np.array.arange(numeros)
print("Arrays ordenados: ",orden)
print(orden)

print(max(numeros))

print(min(numeros))
