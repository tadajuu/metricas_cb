import math
a = float(input("Digite a distancia a: "))
b = float(input("Digite a distancia b: "))
gama = float(input("Digite o angulo v em graus: "))
gama_rad = math.radians(gama)
c = math.sqrt(a**2 + b**2 - 2*a*b*math.cos(gama_rad))
print(round(c, 2))