import math

raio = float(input())

area = math.pi * raio **2
volume = 4 * (math.pi * raio ** 3) / 3 

print(round(area, 3))
print(round(volume, 3))