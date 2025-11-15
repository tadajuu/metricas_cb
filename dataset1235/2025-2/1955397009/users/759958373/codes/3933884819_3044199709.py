import math

pessoas = int(input())
proba = (1 - math.factorial(365)/math.factorial(365-pessoas) * 1/365**pessoas) *100

print(round(proba, 2))