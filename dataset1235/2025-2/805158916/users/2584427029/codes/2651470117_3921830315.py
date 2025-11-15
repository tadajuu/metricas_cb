litros = float(input())

preco_gasolina = 2.86
servico_oleo = 50.00
valor_sem_icms = (litros * preco_gasolina) + servico_oleo
valor_total = valor_sem_icms * 1.34
print(f"{valor_total:.2f}")