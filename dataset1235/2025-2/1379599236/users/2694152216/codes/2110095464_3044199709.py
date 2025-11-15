import math
n = int(input("Digite o número de pessoas no grupo: "))
result = 1 - (math.factorial(365) / math.factorial(365-n) * (1/365**n))
result2 = result*100

print(round(result2, 2))