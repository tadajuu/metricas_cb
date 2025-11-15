import math

x = float(input("Insira a distância de A: "))
y = float(input("Insira a distância de B: "))
z = float(input("Insira o valor do ângulo entre A e B: "))

g = math.radians(z)
j = math.sqrt(x**2+y**2-2*x*y*(math.cos(g)) )

print(round(j,2))