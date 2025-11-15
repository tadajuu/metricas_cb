import math

r = float(input())
area_circulo = math.pi * (r ** 2)
volume_esfera = (4/3) * math.pi * (r ** 3)

print(round(area_circulo, 3))
print(round(volume_esfera, 3))
