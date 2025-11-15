import math
n = int(input())
p = (1 - (math.factorial(365)/(math.factorial(365-n))) * 1/(365**n))*100
print(round(p,2))