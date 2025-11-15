import math
a = float(input("distância a entre observador e primeira arvore: "))
b = float(input("distância b: "))
ya = float(input("ângulo y: "))
y = math.radians(ya)
c = math.sqrt(a**2+b**2-2*a*b*math.cos(y))
print(round(c,2))