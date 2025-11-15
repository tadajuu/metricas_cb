import math

# faça seu código aqui!

lado = int(input("Insira a Distancia "))

apotema =  lado / (2 * math.tan(math.pi/9))
area = (9*lado*apotema) / 2
print(round(area,2))
