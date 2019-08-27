import numpy as np

x = input("Inserte el 100% de los valores: ")
y = input("Inserte el valor del cual desea saber el porcentaje: ")

cienValor= int(x)
valorConocer= int(y)
resultado = 100*valorConocer/cienValor

print("El valor en porcentaje de ",valorConocer," es: ",resultado)
