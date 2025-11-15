from math import *

# faça seu código aqui!
ld = float(input("Digite o lado:"))

Apotema = ld /( 2*tan (pi/11))
area = 11/2 * ld * Apotema
print(round(area,2))