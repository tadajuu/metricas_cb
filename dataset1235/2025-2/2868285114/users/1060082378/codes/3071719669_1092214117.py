valor_pedagio = 9.80
taxa_fixa = 20.00
quantidade_de_pedagios = float(input())
total_sem_imposto = valor_pedagio + taxa_fixa * quantidade_de_pedagios
total_com_imposto = valor_pedagio + taxa_fixa * quantidade_de_pedagios * 0.15
print(round(total_com_imposto, 2))
