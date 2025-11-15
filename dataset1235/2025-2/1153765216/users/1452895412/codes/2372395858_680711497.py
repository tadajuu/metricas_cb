import math
lado = float(input(print("Digite o comprimento do lado: ")))
area = (3 * (lado ** 2)) / (math.tan(math.pi / 12))
print(round(area, 2))