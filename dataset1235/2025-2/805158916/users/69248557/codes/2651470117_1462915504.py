import math
# faça seu código aqui!

comp_l = float(input("Comprimento dos lados do pentagolo "))
apotema = comp_l/(2*math.tan(math.pi/5))
area = (5 *comp_l* apotema)/2
print(round(area, 2))
