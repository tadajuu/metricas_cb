import math
lado = float(input("Qual o valor do lado?: "))
apotema = lado / 2 * math.tan(math.pi / 8)
area = 4 * lado * apotema
print(round(area, 2))