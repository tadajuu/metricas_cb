from math import tan, radians

lado = float(input('qual o comprmento de um lado?:'))
apotema = lado/ (2*tan(radians(36)))
area = 5 * lado * apotema /2

print(round(area , 2))