litros = float(input("informe a quantidade de litros abastecidos: "))
preco_gasolina = 2.86
troca_oleo = 50.0
icms = 34/100

total_sem_icms = litros * preco_gasolina + troca_oleo
total_com_icms = total_sem_icms * (1 + icms)

print(round(total_com_icms, 2))