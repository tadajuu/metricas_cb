import math
a= float(input("digite o tamanho de a:"))
b= float(input("digite o tamanho de b:"))
gama= float(input("digite o tamanho de gama:"))
cos= math.cos(math.radians(gama))
c= math.sqrt((a**2)+(b**2)-2*a*b*cos)
print(round(c,2))