
import math
# faça seu código aqui!
lado = float(input())

apotema = lado/(2*math.tan(math.pi/5))
area = (5/2) * lado * apotema

print (round(area,2))