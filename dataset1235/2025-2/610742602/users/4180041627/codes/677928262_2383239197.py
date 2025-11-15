from math import *
A= float(input("insira a quantidade de A;"))
B= float(input("insira a quantidade de B;"))
G= float(input("insira a quantidade do angulo;"))

J=radians(G)

C=sqrt((A**2)+(B**2)-2*A*B*cos(J))

print(round(C,2))