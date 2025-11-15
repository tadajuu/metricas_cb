import math

n = int(input("Qual o número de pessoas? "))

prob_dif = math.factorial(365)/(math.factorial(365-n)* (365**n))
prob = (1 - prob_dif)*100

print(round(prob,2))