from math import *

# Entrada
Lado = int(input("Digite a medida do lado do octógono:"))
Denominador = float(2*tan(pi/8))
Apotema = Lado/Denominador
Área = 4*Lado*Apotema
#Saída
print(Lado)
print(round(Apotema,2))
print(round(Área,2))