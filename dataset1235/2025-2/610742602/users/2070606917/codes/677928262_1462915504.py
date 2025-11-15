from math import tan, radians

lado = float(input('Digite o cmprimento do lado do pentágono: '))

apotema = lado / (2 * tan(radians(36)))

area = (5 * lado * apotema) / 2

print(round(area, 2))

# faça seu código aqui!