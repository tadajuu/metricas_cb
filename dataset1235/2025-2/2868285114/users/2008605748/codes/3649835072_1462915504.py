import math
lado = float(input("Digite o comprimento do lado do pentagono: "))
apotema = lado / (2 * math.tan(math.pi / 5))
area = (5 * lado * apotema) / 2
print("A area do pentagono e:", round(area, 2))