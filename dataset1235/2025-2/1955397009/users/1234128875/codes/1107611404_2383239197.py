from math import * 

distanciaA = float(input())
distanciaB = float(input())
angulo = float(input())
angulo = radians(angulo)

c = ((distanciaA ** 2) + (distanciaB ** 2) ) - ((2 * distanciaA * distanciaB)*cos(angulo))
c = c ** (1/2)
print(round(c, 2))