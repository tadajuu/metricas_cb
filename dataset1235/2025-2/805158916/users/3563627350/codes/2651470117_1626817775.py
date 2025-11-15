import math

r = float(input())

area = math.pi * (r **2)
volume = (4/3) * math.pi * (r **3)

print(round(area, 3))
print(round(volume, 3))