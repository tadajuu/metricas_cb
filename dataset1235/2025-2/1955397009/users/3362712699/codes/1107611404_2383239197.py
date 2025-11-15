import math

a = float(input("Qual a medida do lado a? "))
b = float(input("Qual a medida do lado b? "))
y = float(input("Qual a medida do ângulo entre os ladoa a e b "))

c = math.sqrt(a**2 + b**2 - 2*a*b* math.cos(math.radians(y)))

print(round(c, 2))