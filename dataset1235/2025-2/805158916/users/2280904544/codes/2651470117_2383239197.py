from math import *

a = float(input()) 
b = float(input()) 
y = float(input())

cc = sqrt(pow(a,2)+pow(b,2) - 2*a*b*cos(radians(y)))

print(round(cc,2))