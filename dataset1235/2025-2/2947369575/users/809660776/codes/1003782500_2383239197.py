import math

a = float(input("informe a distancia até a primeira arvore: "))
b = float(input("informe a distancia ate a segunda arvore: "))
gamma = float(input("informe o angulo entre as duas distancias (em graus): "))

gamma_rad = math.radians(gamma)

c = math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(gamma_rad))

print(round(c, 2))