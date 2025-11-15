valor = float (input("Digite o valor:"))
consumo = 0.43 * valor
taxa_fixa = 10.00
sem_icms = consumo + taxa_fixa
icms = sem_icms + (25/100) 
valor_total = icms + sem_icms

print(round(valor_total, 2))