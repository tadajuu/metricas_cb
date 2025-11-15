from math import *

# faça seu código aqui!
x=float(input("insira o lado do pentagono: "))
apotema= x/(2*tan(pi/5))
area= (5/2)*x*apotema
print(round(area,2))