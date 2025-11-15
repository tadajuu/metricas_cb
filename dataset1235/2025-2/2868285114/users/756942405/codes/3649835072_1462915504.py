from math import *

comprimento = int(input("comprimeto: "))
apotema = comprimento/( 2*tan(pi/5))
a = (5/2 * comprimento * apotema)
print(round(a, 2))