from math import *

N = int(input("Numero de pessoas: "))
dias = factorial(365)
diasN = factorial(365-N)
diasP = 365**N
pn = (1-dias/diasN*1/diasP) * 100

print(round(pn, 2))