import math

# faça seu código aqui!
lado=float(input())
apo = lado/(2 *math.tan(math.pi/11))
area = (11/2)*lado*apo
print(round(area,2))