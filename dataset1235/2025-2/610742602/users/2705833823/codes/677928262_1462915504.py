lado = float(input("Insira o comprimento do lado do pentagono"))

import math
apotema = lado/ (2 * math.tan(math.pi/5))
area = 5/2 * lado * apotema

print(round(area,2))