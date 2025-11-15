import math
raio = float(input("Digite o valor do raio"))
area_circulo = math.pi * raio ** 2
volume_esfera = ((4 / 3) * math.pi * raio ** 3)
print(round(area_circulo, 3))
print(round(volume_esfera, 3))