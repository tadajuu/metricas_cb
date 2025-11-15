from math import*
comprimento_do_lado = float(input())

apotema = comprimento_do_lado / (2*tan(pi/11))
area = (11 * comprimento_do_lado * apotema) / 2

print(round(area,2))