import math 

a = float(input())
b = float(input())
angulo = float(input())

angulo_rad = math.radians(angulo)
c = math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(angulo_rad))
print(f"c={c:.2f}")