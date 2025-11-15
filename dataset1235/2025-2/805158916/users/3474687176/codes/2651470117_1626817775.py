import math

raio = float(input(''))

area = round(math.pi * raio**2 , 3)
volume = round((4/3) * math.pi * raio**3 , 3)

print(area)
print(volume)