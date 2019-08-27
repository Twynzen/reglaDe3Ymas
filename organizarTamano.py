import numpy as np

x= input("Inserte la cantidad de números que se calculan: ")
cantidadNumeros= int(x)
numeros = np.arange(cantidadNumeros)

for numero in numeros:

    numeros[numero]= int(input("Inserte el número : "))
