from math import *

lado = float(input("Informe o tamanho do lado: "))

den = 2 * tan(pi/10)

apot = lado/den

area = 5 * lado * apot

area_arredondada = round(area, 2)

print(area_arredondada)

