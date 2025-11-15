import math
# faça seu código aqui!
pentagon_side = float(input("Informe o valor do lado do pentagono: "))

apotema = pentagon_side / (2 * (math.tan(math.pi/5)))
pentagon_area = (5/2) * pentagon_side * apotema

print(round(pentagon_area,2))