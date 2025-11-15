litros = float(input("Digite quantos litros deseja: "))
litro_gasolina = 2.86
troca_oleo = 50.00
valor_abastecimento = litros * litro_gasolina
total = troca_oleo + valor_abastecimento
valor_total = total * 1.34
valor_total_arredondamento = round(valor_total, 2)
print(valor_total_arredondamento)