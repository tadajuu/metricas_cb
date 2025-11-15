import math
#Agr que eu apanho
a = float(input())

b = float(input())

ang = float(input())

c = round((a**2 + b**2 -2*a*b *math.cos(math.pi*ang/180))**0.5,2)
print(c)