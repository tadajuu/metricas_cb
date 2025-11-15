import math
distancia_a = float(input("Distância entre você e a primeira árvore: "))
distancia_b = float(input("Distância entre você e a segunda árvore: "))
gamma = float(input("Ângulo y entre a e b (em graus): "))

gamma_rad = math.radians(gamma)
c = math.sqrt(distancia_a**2 + distancia_b**2 - 2 * distancia_a * distancia_b * math.cos(gamma_rad))
print(round(c,2))