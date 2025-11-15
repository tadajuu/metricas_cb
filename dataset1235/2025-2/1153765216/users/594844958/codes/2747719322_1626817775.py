import math

raio = float(input())

area = raio*raio*math.pi

volume = (raio**3*math.pi*4) / 3

print(round(area, 3))
print(round(volume, 3))