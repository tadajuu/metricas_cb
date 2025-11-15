import math

ax = float(input("Informe a coordenada X de A: "))
ay = float(input("Informe a coordenada Y de A: "))
bx = float(input("Informe a coordenada X de B: "))
by = float(input("Informe a coordenada Y de B: "))

distancia = math.sqrt((bx-ax)**2 + (by-ay)**2)

print(round(distancia,3))