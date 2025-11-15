litros = float(input())
preco_gasolina = 2.86
servico_troca_oleo = 50.00
icms = 34/100
subtotal = litros * preco_gasolina + servico_troca_oleo
total = subtotal * (1 + icms)
print(round(total, 2))