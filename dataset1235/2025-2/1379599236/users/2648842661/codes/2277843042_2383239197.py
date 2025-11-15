from math import*

a = float(input("Digite a distancia a (observador ate a primeira arvore):"))
b = float(input("Digite a distancia a (observador ate a primeira arvore):"))
gamma_graus= float(input())

gamma_radianos =  radians(gamma_graus)

c= sqrt(a**2 + b**2 - 2*a*b*cos(gamma_radianos))
print(round(c,2))
