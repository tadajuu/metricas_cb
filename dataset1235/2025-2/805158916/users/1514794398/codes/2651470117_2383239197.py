distA = float(input("digite a distância a: "))
distB = float(input("digite a distância b: "))
angAB = float(input("digite o ângulo entre a e b: "))       
import math
ang = math.radians(angAB)
c = (math.sqrt(distA**2 + distB**2 - 2*distA*distB*math.cos(ang)))
print(round(c,2))