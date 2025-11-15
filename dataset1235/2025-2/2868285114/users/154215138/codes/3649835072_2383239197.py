import math
a = float(input("Digite o lado a: "))
b = float(input("Digite o lado b: "))
gamma = float(input("Digite o ângulo: "))
gama_rad = math.radians(gamma)
c = (a ** 2 + b ** 2 - 2*a*b*math.cos(gama_rad))**0.5
c_arredondamento = round(c, 2)
print(c_arredondamento)