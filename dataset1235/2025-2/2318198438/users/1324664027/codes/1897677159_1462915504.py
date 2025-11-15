from math import pi, tan

# faça seu código aqui!

l = float(input("Lado: "))

ap = l/(2*tan(pi/5))
A = (5/2)*l*ap

print(round((A), 2))