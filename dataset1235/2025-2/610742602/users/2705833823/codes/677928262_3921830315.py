preço = float(input("Insira a quantidade abastecida:"))

preço_litro = 2.86
preço_oleo = 50.00
icms = 34/100

gasolina = preço * preço_litro
serviço = gasolina + preço_oleo
total = serviço * (1 + icms)

print(round(total,2))