import math
a = float(input("Digite a distancia a: "))
b = float(input("Digite a distancia b: "))
gamma_graus = float(input("Digite o angulo gamma em graus: "))

gamma_radianos = math.radians(gamma_graus)

c = math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(gamma_radianos))

print(f"A distancia entre as arvores e:{c:.2f}")