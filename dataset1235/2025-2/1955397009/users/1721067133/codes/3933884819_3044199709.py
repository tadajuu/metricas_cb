from math import *

n = int(input())

p2 = (factorial(365)) / (factorial(365-n))
p3 = 1 / (365**n) 
p = 1 - (p2 * p3)

print(round(p,4)*100)                                            