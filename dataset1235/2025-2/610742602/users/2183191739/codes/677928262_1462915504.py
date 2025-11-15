from math import *
import math
z= math.tan(pi/5)
# faça seu código aqui!
x= float(input("digite o comprimento do lado do seu pentagono: "))
h= x/(2*z)
a= 5/2 * x * h
print(round(a,2))