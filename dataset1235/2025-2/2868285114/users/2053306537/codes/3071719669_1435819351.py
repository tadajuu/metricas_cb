peso_saco = float(input())
quantidade_diaria = float(input())
consumo_total = quantidade_diaria * 5
restante = peso_saco - consumo_total
print(f"{restante: .2f}")