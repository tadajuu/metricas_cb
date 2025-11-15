import math as m

lado = float(input())

apotema = lado/(2*(m.tan(m.pi/5)))

area = lado*apotema * (5 / 2)

print(round(area, 2))