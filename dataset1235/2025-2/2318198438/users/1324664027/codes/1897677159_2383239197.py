a = float(input("a: "))
b = float(input("b: "))
y = float(input("y: "))

from math import cos, radians
x = radians(y)
c = (a**2 + b**2 - 2*a*b*cos(x))**(1/2)

print(round((c), 2))