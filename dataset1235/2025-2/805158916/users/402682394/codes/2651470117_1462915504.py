from math import pi 
from math import tan 


# faça seu código aqui!
T = 2*tan(pi/5)
Lado = float(input("Informe o lado do pentágono:"))

Apotema = Lado/(2*T)
Area = 5*Lado*Apotema

print(round(Area,2))