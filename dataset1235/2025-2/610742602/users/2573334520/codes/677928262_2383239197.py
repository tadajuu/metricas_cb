from math import *
a=float(input())
b=float(input())
c=float(input())
r=radians(c)
k=sqrt(a**2+b**2-2*a*b*cos(r))
print(round(k,2))