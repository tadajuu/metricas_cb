import math 
# Lendo o comprimento do lado do pentagono
lado = float(input())
# Calculando a apotema
apotema = lado / (2 * math.tan(math.pi / 5))
# Calculando a area do pentagono
area = (5 * lado * apotema) / 2
# Imprimindo a area arredondada para 2 casas decimais 
print(round(area, 2))