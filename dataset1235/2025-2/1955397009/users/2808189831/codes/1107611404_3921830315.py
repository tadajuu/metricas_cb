litros = float(input())

preco_litro = 2.86
troca_oleo = 50.0

valor_sem_imposto = litros * preco_litro + troca_oleo

valor_total =valor_sem_imposto * 1.34

print(f"{valor_total:.2f}")