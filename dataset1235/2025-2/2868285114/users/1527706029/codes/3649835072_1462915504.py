from math import pi,tan

#entrada
lado = float(input())

#processamento
apotema = lado/(2*tan(pi/5))
area = 5/2*lado*apotema

#saida
print (round(area,2))

