litros = float(input(""))
preco_gasolina = 2.86
troca_oleo = 50.00
valor_abastecido = litros * preco_gasolina
subtotal = valor_abastecido + troca_oleo
total_com_icms = subtotal * (1 + 34 / 100)
print(round(total_com_icms, 2))