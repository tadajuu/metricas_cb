import math
distancia_a = float(input("Distancia entre você e a primeira arvore:"))
distancia_b = float(input("Distancia entre você e a segunda arvore:"))
gamma = float(input("Angulo y entre a e b (em graus):"))

gamma_rad = math.radians(gamma)
c = math.sqrt(distancia_a**2 + distancia_b**2 - 2 * distancia_a * distancia_b* math.cos(gamma_rad))
print(f"{c:.2f}")