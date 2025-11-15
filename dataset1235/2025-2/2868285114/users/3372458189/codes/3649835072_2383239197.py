distA = float(input("Distancia a: "))
distB = float(input("Distancia b: "))
anguloab = float(input("Angulo: "))
import math
cos = math.cos(math.radians(anguloab))
formula = distA**2+distB**2-2*distA*distB*cos
raiz4 = math.sqrt(formula)
c = raiz4
print(round(raiz4, 2))