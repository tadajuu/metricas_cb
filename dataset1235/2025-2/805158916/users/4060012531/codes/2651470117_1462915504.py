from math import tan, pi
# faça seu código aqui!
lado=float(input())
ang_penta=pi/5
apotema=lado/(2*tan(ang_penta))
area=(5/2)*lado*apotema
print(round(area,2))
