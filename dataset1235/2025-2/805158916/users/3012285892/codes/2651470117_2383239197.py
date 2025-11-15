a = float(input("Distância a:"))
b = float(input("Distância b:"))
y = float(input("Ângulo entre a e b (em graus):"))

import math

c = math.sqrt((a**2)+(b**2)-2*(a*b)*math.cos(math.radians(y)))
print(round(c,2))