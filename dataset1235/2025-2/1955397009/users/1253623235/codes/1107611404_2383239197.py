from math import*

X = float(input("Distancia a: "))
Y = float(input("Distancia b: "))
Z = float(input("Angulo entre a e b: "))

s = X**2
d = Y**2
h = 2*X*Y*cos(radians(Z))



dist = sqrt(s + d - h)


print(round(dist, 2))