from math import pi, tan

# faça seu código aqui!
lado=int(input())

ang=pi/9

apot=lado/(2*tan(ang))

area=9/2*lado*apot

print(round(area,2))