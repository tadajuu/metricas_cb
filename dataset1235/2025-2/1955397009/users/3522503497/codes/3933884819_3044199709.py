from math import*

n=int(input())

p=(1-(factorial(365)/factorial(365-n)/(365**n)))*100

print(round(p,2))