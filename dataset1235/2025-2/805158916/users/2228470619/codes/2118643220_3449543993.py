import math
lado = float(input("Digite o tamanho do lado: "))
angulo = math.pi/10
apot = (lado)/(2*(math.tan(angulo)))
area = 5*lado*apot

print("A área do decágono é: ",round(area,2))