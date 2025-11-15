from math import pi , tan

# faça seu código aqui!
lado=float(input(":"))
apotema=lado/(2*tan(pi/9))

print(round((9/2)*lado*apotema,2))