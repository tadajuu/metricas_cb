from math import *

t1 = radians(float(input("Latitude do ponto P1: ")))
g1 = radians(float(input("Longitude do ponto P1: ")))
t2 = radians(float(input("Latitude do ponto P2: ")))
g2 = radians(float(input("Longitude do ponto P2: ")))
R = 6371.01

dist =  R * acos( sin(t1)*sin(t2) + cos(t1)*cos(t2)*cos(g1 - g2))

print (round(dist,2))