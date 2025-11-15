from math import *

#Informações iniciais
lado_decagono = float(input())

#Calculo
apotema = lado_decagono / (2 * tan(pi/10))
area_decagono = 5 * lado_decagono * apotema

#Assim
print(round(area_decagono,2))