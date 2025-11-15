from math import pi, tan

# faça seu código aqui!

lado = float(input())

apotema = (lado)/(2*tan(pi/9))

A = float((9/2)*lado*apotema)

print(round(A, 2))

