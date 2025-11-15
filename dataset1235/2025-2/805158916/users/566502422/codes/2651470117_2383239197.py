distA = float(input("digite a distancia a"))
distB = float(input("digite a distancia b"))
angAB = float(input("digite o angulo entre a e b"))
import math
ang = math.radians(angAB)
c = (math.sqrt(distA**2 + distB**2 - 2*distA*distB*math.cos(ang)))
print(round(c,2))