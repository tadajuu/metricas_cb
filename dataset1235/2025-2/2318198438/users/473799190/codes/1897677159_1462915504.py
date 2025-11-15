import math

# faça seu código aqui!
LadoA = float(input())

p = math.pi
tan = math.tan(p/5)
apotema = LadoA/(2 * tan)
area = (5/2)*(LadoA*apotema)

print(round(area, 2))