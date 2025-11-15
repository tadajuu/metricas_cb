valor = float(input(("Quantidade de litros de gasolina abastecidos:")))
litro = 2.86
oleo = 50.00
icms = 34 / 100
gasolina = valor * litro
serviço = gasolina + oleo
total = serviço * (1 + icms)
print(round(total, 2))