distanA = float(input("digite a distancia a"))
distanB = float(input("digite a distancia b"))
angAB = float(input("digite o angulo entre a e b"))
import math
ang = math.radians(angAB)
c =(math.sqrt(distanA**2+ distanB**2 - 2*distanA*distanB*math.cos(ang)))
print(round(c,2))