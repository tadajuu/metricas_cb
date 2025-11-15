qtde_litros = float(input())

gasolina = qtde_litros * 2.86
total_sem_imcs = gasolina + 50
total_com_imcs = total_sem_imcs * 1.34

print(round(total_com_imcs, 2))