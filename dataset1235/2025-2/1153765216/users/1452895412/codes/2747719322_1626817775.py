import math
raio = float(input(print("Digite o raio: ")))
area = math.pi * (raio ** 2)
volume = 4 / 3 * math.pi * (raio ** 3)
print(round(area, 3))
print(round(volume, 3))