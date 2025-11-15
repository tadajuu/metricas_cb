from math import *

# faça seu código aqui!
import math

lado = float(input(" Informe o comprimento dos  lados:"))

apotema = lado / (2 * math.tan ( math.pi / 7))
area = 7/2 * lado * apotema
print(" A sua área é: ")
print(round(area,2))