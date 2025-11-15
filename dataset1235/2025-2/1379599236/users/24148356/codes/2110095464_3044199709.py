import math
numero_de_pessoas = int(input())
p = (1 - (math.factorial(365) / math.factorial(365 - numero_de_pessoas) * (1 / 365**numero_de_pessoas)))*100
print(round(p, 2))