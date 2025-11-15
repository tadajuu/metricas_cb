import math 

a = float(input("Informe a distância entre o observador e a primeira árvore: "))
b = float (input("Informe a distância entre o observador e a segunda árvore: "))
y = float(input("Informe o ângulo entre as retas: "))

radiano = math.radians(y)

cos = math.cos(radiano)

radicando = a**2 + b**2 - 2 * a * b * cos

distancia = radicando**0.5

distancia_arredondada = round (distancia, 2)

print(distancia_arredondada)
