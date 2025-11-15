from math import *

# faça seu código aqui!

lado = float(input("Digite o lado do pentagono: "))

apotema = float(lado/(2*(tan(pi/5))))
area = (5/2)*lado*apotema

print(round(area,2))