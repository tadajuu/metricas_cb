preco_gasolina = 2.86
servico_troca_oleo = 50.00
icms = 0.34

litros = float(input("Digite a quantidade de litros abastecidos: "))

valor_gasolina = litros * preco_gasolina
subtotal = valor_gasolina + servico_troca_oleo

total_com_icms = subtotal * (1 + icms)

print(f"Valor total a ser pago: R${total_com_icms: .2f}")