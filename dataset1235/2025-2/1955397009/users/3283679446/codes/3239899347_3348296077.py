horas = float(input("Informe o tempo em horas: "))

valor_sem_imposto = 5 + 15 * horas

total = valor_sem_imposto * 1.20

total_arredondado = round(total, 2)

print(total_arredondado)

