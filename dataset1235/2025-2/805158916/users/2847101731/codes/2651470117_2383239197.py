import math
a= float(input("aa"))
b= float(input("bb"))
c= float(input("cc"))

rad= math.radians(c)

d=(math.sqrt(a**2+b**2-2*a*b*math.cos(rad)))
print(round(d,2))
