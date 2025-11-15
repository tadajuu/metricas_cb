#Quantidade de litros abastecidos
gas = float(input("Litros de gasolina: "))
#Fórmula
total = gas * 2.86 + 50
imp = total + (total * (34/100))
#Valor a ser pago
print(round(imp,2))