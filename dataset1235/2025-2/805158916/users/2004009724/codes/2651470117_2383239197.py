import math 
a = float(input())
b = float(input())
gramma_graus = float(input())
gramma_rad = math.radians (gramma_graus)
c = math.sqrt(( a ** 2 ) + (b ** 2) - (2 * a * b * math.cos ( gramma_rad)))
print(round(c, 2))
