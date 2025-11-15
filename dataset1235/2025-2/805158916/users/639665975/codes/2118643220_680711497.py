import math

# faça seu código aqui!
lado = float(input("Comprimento do lado de seu dodecágono:"))
apotema = (lado)/(2*math.tan(math.pi/12))

area = apotema*6*lado
print(round(area,2))