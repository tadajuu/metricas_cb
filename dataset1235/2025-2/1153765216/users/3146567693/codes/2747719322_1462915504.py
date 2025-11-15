from math import  *
import math 

lado = int(input("digite o comprimento do lado do Pentágono: "))

x = math.tan(pi/5)

apotema = lado/(2*x)
área = 5/2 * lado * apotema

print(round(área,2))
# faça seu código aqui!