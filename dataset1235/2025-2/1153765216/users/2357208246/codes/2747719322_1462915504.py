import math
pi = math.pi
# faça seu código aqui!
comprimento_lado = float(input())
apotema = (comprimento_lado / (2 * math.tan(pi/5)))
area = (5/2) * comprimento_lado * apotema

print(round(area, 2))