from math import *

a = float(input("Informe o valor da distância a entre o observador e aprimeira arvore: "))
b = float(input("Informe o valor da distância b entre o observador e a segunda arvore: "))
y = float(input("Informe o angulo y entre a e b em graus: "))
y = radians (y)

c = sqrt( ((a**2) + (b**2)) - ((2*a*b)*(cos(y))) )

print(round(c,2))

# SEMPRE QUE PEDIR ANGULO EM GRAUS CONVERTER COM A FUNÇAO RADIANS