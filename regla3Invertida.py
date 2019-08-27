import numpy as np

x = input("Inserte el 100% de los valores: ")
y = input("Inserte el porcentaje que desea conocer:")

cienValor= int(x)

porcentajeConocer= int(y)
resultado = cienValor*porcentajeConocer/100

print("El porcentaje de ",porcentajeConocer," es: ",resultado)
