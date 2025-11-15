litros = float(input())
preço_gasolina = 2.86
preço_oleo = 50.00
custo_gasolina = litros * preço_gasolina
total_sem_imposto = custo_gasolina + preço_oleo
total_com_imposto = total_sem_imposto * 1.34
print(round(total_com_imposto, 2))


