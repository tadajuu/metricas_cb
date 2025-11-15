litros = float(input("Digite a quantidade de litros abastecidos: "))

preco_gasolina = 2.86 
troca_oleo = 50.00
icms = 34

valor_abastecimento = litros * preco_gasolina

total_sem_icms = valor_abastecimento + troca_oleo

valor_total = total_sem_icms * (1 + icms / 100)

print(round(valor_total, 2))