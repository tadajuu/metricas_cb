import math
distancia_a = float(input("a: "))
distancia_b = float(input("b: "))
angulo = float(input("angulo: "))

gama_rad = math.radians(angulo)

c = math.sqrt(distancia_a**2 + distancia_b**2 - 2*distancia_a*distancia_b*math.cos(gama_rad))
print(round(c, 2))