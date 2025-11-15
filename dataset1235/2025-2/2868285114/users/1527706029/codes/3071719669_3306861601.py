from math import pi,tan

lado = float(input())
apotema = lado/(2*tan(pi/9))
area = (9/2)*lado*apotema

print(round(area,2))