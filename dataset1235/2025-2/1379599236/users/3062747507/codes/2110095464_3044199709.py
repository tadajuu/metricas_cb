from math import *
n = int(input())
pn = (factorial(365))/(factorial(365 - n)) * 1 / (365)**n 
por = (1 - pn) * 100
print(round(por ,2))