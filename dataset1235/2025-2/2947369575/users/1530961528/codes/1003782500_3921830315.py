qtde_litros = float(input())

gasolina = qtde_litros * 2.86
total_sem_icms = gasolina + 50
total_sem_icms = total_sem_icms * 1.34

print(round(total_sem_icms, 2))