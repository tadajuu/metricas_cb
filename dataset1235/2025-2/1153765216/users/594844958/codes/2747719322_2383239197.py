import math as m

a = float(input())
b = float(input())
y = float(input())

sem_raiz = (((a**2) + (b**2)) - (2*a*b*m.cos(m.radians(y))))
distancia = m.sqrt(sem_raiz)

print(round(distancia, 2))