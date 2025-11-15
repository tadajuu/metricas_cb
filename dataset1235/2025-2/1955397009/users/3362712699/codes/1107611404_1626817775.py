import math

r = float(input("Qual a medida do raio?"))

a = round(math.pi*r**2, 3)
v = round((4/3)*math.pi*r**3, 3)

print(round(a, 3))
print(round(v, 3))