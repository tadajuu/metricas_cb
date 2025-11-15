from math import * 

t1 = radians(float(input()))
g1 = radians(float(input()))
t2 = radians(float(input()))
g2 = radians(float(input()))

r = 6371.01

d = r*acos((sin(t1) * sin(t2)) + cos(t1) * cos(t2) * cos(g1-g2))

print(round(d,2))