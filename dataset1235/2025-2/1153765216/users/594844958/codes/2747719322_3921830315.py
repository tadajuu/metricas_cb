litros_abastecidos = float(input())

valor_sem_impostos = 2.86*litros_abastecidos + 50
valor_total = valor_sem_impostos + ((34/100) * valor_sem_impostos)

print(round(valor_total, 2))