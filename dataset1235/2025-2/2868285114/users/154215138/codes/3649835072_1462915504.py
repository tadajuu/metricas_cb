import math
lado = float(input("Digite o lado:"))
apotema = lado / (2 * math.tan(math.pi / 5))
area = (5/2) * lado * apotema
area_arredondamento = round(area, 2)
print(area_arredondamento)