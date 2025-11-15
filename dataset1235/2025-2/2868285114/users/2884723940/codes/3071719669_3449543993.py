import math 

# faça seu código aqui!
lado = int(input())

apotema = lado / (2 * math.tan(math.pi/10))
area = 5 * (lado * apotema)
print(round(area,2))