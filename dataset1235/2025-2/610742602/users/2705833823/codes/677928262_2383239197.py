import math
a = float(input("Insira a distancia da primeira arvore:"))
b = float(input("Insira a distancia da segunda arvore:"))
ang = float(input("Angulo entre as duas distancias:"))

rad = math.radians(ang)
c = math.sqrt(a ** 2 + b ** 2 - 2 *a * b *math.cos(rad))

print(round(c,2))