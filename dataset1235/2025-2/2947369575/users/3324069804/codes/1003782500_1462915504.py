from math import *

# faça seu código aqui!
lado= float(input("digete um valor para o lado:"))

apotema= lado/(2*(tan(pi / 5)))

A= 5/2 * lado * apotema

print(round(A, 2))