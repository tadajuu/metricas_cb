gasolina = 2.86
servico = 50.00
litros = float(input("informe a qtd de litros abastecidos: "))
formula = (litros*gasolina) + servico
total = formula + formula*(34/100)
print(round(total, 2))