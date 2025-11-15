import math

pessoas = int(input("Informe o numero de pessoas: "))
fac1 = math.factorial(365)
fac2 = math.factorial(365-pessoas)
prob = 1-(fac1/fac2)*(1/(365**pessoas))
porcento = prob*100
print(round(porcento,2))
