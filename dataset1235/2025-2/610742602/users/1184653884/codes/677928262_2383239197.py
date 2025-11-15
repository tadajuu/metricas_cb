a=float(input("distancia entre voce a 1 arvore?"))
b=float(input("distancia entre voce e 2 arvore?"))
c=float(input("angulo entre a e b?"))
import math

ang=math.radians(c)

cs=math.cos(ang)
f=(a**2+b**2-2*a*b*cs)**0.5
print(round(f,2))