import math

lado = float(input("Digite o lado:"))
# faça seu código a
octogono = lado / (2* math.tan(math.pi/8))

var = 4 * lado * octogono

print(round(var, 2))