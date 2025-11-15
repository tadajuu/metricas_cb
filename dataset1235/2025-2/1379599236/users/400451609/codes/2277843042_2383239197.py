import math

a = float(input("Qual a distância entre o observador e a primeira árvore? "))
b = float(input("Qual a distância entre o observador e a segunda árvore? "))
grau = float(input("Qual o ângulo entre a e b? "))

grau = math.radians(grau)

c = math.sqrt(a**2+b**2-2*a*b*math.cos(grau))

print(round(c,2))