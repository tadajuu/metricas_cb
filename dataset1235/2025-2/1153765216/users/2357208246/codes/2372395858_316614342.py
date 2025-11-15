import math
pi = math.pi
tan = math.tan

comprimento_do_lado = float(input())
apotema = (comprimento_do_lado) / (2 * (tan(pi/7)))

area = (7/2) * comprimento_do_lado * apotema

print(round(area, 2))