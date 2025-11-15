import math

a = float(input("Digite a distancia ate a  primeira arvore: "))
b = float(input("Digite a dsitancia ate a primeira arvore: "))
g = float(input("Digite o angulo entre as distancias em graus: "))

g_rad = math.radians(g)

c = math.sqrt(a**2 + b**2 - 2*a*b*math.cos(g_rad))

print(round(c, 2))