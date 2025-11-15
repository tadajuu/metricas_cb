import math

dA = float(input("Distancia 1: "))
dB = float(input("Distancia 2: "))
angGraus = float(input("Angulo: "))

def distancia(dA, dB, ang):
  rad = math.radians(ang)
  res = math.sqrt((dA**2) + (dB**2) - (2*dA*dB*math.cos(rad)))
  return res

res = distancia(dA, dB, angGraus)
print(round(res, 2))
  