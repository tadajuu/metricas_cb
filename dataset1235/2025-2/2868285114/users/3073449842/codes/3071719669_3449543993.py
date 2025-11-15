import math
pi = math.pi
tag = math.tan(pi/10)
lado = float(input("Digite o comprimento do lado: "))
apotema = lado / (2*tag)
area = 5*lado*apotema
print(round(area,2))
# faça seu código aqui!