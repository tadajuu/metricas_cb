quantidade = float(input("Qual a quantidade de litros abastecidos?: "))

gasolina = quantidade * 2.86

ICMS = 34/100

aumento = (gasolina + 50.0) * ICMS

total = gasolina + 50.0 + aumento

print(round(total, 2))