from math import *

t1 = float(input("t1: "))
g1 = float(input("g1: "))
t2 = float(input("t2: "))
g2 = float(input("g2: "))

arcos = acos(sin(radians(t1)))
sin = sin(radians(t2))
cos1 = cos(radians(t1))
cos2 = cos(radians(t2))
cos3 = cos(radians(g1-g2))
R = 6371.01

print(round(R*arcos*sin+cos1*cos2*cos3, 2))
          