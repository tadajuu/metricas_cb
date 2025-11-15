from math import *
# Entrada 
lado = int(input("Para calcular a área do pentágono, digite o número de lados:"))
apotema = lado / (2 * tan(pi/5))
area = 5/2 * lado * apotema 

# Saída 
print(round(area,2))