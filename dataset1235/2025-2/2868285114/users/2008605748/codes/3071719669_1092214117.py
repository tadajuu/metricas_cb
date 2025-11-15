praca = int(input())
total_sem_imposto = (praca * 9.80) + 20
total_final = total_sem_imposto * 1.15
print(round(total_final, 2))