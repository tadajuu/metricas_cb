import math
dA = float(input("Distancia A: "))
dB = float(input("Distancia B: "))
gamma = float(input("Angulo A e B: "))

dC = math.sqrt(dA**2 + dB**2 - 2* dA * dB * math.cos(math.radians(gamma)))
print(round(dC , 2))