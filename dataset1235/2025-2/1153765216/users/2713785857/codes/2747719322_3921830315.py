caso1 = float(input("quantidade de litros: "))
gasolina = 2.86*caso1
oleo = 50.0
total = gasolina + oleo 
ICMS = total * 34/100
totalreal = total + ICMS 
print(round(totalreal,2))