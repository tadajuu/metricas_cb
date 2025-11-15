litros = float(input("Insira a quantidade de litros abastecidos: "))

preco_gasolina = 2.86
preco_oleo = 50.00

total_sem_imposto = (litros * preco_gasolina) + preco_oleo
total_com_imposto =  total_sem_imposto * 1.34

print(round(total_com_imposto, 2))
