from math import*
x = int(input(" "))

pn = 1 - factorial(365)/(factorial(365 - x)) *1/365**x

y = pn*100


print(round(y, 2))