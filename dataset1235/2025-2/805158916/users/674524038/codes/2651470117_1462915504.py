from math import *

# faça seu código aqui!
import math
lado = float(input("Valor do lado: "))
#Apotema
ap = lado/(2* math.tan(math.pi/5))
#Área do pentagono
pa = (5/2) * lado * ap
#Impressão do resultado
print(round(pa,2))