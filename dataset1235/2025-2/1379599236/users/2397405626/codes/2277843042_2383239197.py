import math

a = float(input("Insira a distancia ate a arvore 1 em metros: "))
b = float(input("Insira a distancia ate a arvore 2 em metros: "))
y = math.radians(float(input("Insira o angulo em graus: ")))

c = (math.sqrt((a**2)+(b**2)-(2*(a*b)*math.cos(y))))

print(round(c,2))