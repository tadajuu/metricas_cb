import math

numero = int(input())

p = 1 - math.factorial(365)/math.factorial(365 - numero) * (1/365**numero)

p = p*100

print(round(p, 2))
