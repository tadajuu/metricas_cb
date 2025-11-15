import math
dist_a = float(input())
dist_b = float(input())
angulo_ab = math.radians(float(input()))

dist_ab = (dist_a**2 + dist_b**2 - 2* dist_a* dist_b * math.cos(angulo_ab))**(1/2)
print(round(dist_ab,2))
