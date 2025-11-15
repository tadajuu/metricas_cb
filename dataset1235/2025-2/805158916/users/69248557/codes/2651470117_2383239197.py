import math
a = float(input("Informe dis1 "))
b = float(input("Informe dis2 "))
graus= float(input("Informe angulo "))

graus = math.radians(graus)

lei = math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(graus))

print(round(lei, 2))