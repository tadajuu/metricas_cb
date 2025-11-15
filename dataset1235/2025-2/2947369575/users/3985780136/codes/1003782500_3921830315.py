quantidade = float(input())

gasolina = 2.86
serviço = 50.00
icms = 34

gasolina_total = quantidade*gasolina
sem_imposto = gasolina_total + serviço
valor_icms = sem_imposto * (icms/100)
total = sem_imposto+valor_icms
print(round(total,2))
