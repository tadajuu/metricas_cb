import math

a = float(input("Digite a distancia ate a arvore a: "))
b = float(input("Digite a distancia ate a arvore b: "))
y = float(input("Digite o angulo entre as arvores em graus: "))
rad = math.radians(y)
c = math.sqrt((a**2)+(b**2)-(2*a*b*(math.cos(rad))))
print(round(c,2))