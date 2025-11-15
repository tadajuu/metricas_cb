from math import tan, radians

# Entrada 
lado = float(input("Digite o comprimento do lado do pentágono: "))

# cálculo da apótema
apotema = lado / (2 * tan(radians(36)))

# Cálculo da área
area = (5 * lado * apotema) / 2

# Saída formatada com duas casas decimais
print(f"A área do pentágono é {area:.2f}")