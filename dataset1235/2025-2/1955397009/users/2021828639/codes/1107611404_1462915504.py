from math import pi,tan


lado = float(input("Digite o valor do lado do pentágono:"))
apotema = lado/(2*tan(pi/5))
area= (5/2)*lado*apotema
print(round(area,2))
