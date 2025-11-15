from math import cos
from math import sqrt
from math import radians

a = float(input("Qual a distância à primeira árvore?" ))
b = float(input("Qual a distância à segunda árvore?" ))
y = radians(float(input("Quando mede o ângulo entre as distâncias em graus? ")))

C = sqrt(a**2+b**2-2*a*b*cos(y))
print(round(C,2))