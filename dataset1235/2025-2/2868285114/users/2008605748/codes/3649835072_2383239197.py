import math
A = float(input("qual e a distancia?"))
B = float(input("qual e a distancia?"))
Y = float(input("qual e o angulo em graus?"))
Y_rad = math.radians(Y)
c = math.sqrt(A**2 + B**2 - 2* A * B * math.cos(Y_rad))
print(round(c, 2))