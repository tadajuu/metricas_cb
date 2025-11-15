import math

a=float(input("Distancia da primeira árvore:"))
b=float(input("Distancia da segunda árvore:"))
ang=float(input("Angulo entre as duas distancias:"))

rad=math.radians(ang)

c=math.sqrt(a**2+b**2-2*a*b*math.cos(rad))

print(round(c,2))