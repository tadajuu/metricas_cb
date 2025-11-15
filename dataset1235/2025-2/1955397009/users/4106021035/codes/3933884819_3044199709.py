import math
n = int(input("Numero: "))

num = math.factorial(365)
den = math.factorial (365-n)

p = 1 - (num/den) * 1/(365**n)  

result = p*100

print(round(result, 2))