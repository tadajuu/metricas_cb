import math

A = float(input("distancia a:"))
B = float(input("distancia b:"))
TETA = float(input("angulo y (em graus):"))
angulo = math.radians(TETA)
C = A**2+B**2 - 2*A*B*math.cos(angulo)
side = math.sqrt(C)


print(round(side,2))