import math

# Entrada do comprimento do lado
lado = float(input())

# Calcular a apótema: apotema = lado / (2 * tan(π/5))
apotema = lado / (2 * math.tan(math.pi / 5))

# Calcular a área: area = (5/2) * lado * apotema
area = (5 / 2) * lado * apotema

# Arredondar para duas casas decimais e imprimir
print(round(area, 2))

