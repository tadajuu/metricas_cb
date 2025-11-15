from math import *

# faça seu código aqui!

lado = float(input("LADO"))

apt1 = float(pi / 7)
apt2 = float(tan (apt1))
apt3 = float(2 * apt2)

apt = float(lado / apt3)

area = float(3.50 * lado * apt)

print (round(area,2))