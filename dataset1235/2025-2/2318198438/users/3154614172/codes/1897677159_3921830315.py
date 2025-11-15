litros_abastecidos = float(input('Informe os litros abastecidos'))
troca_de_oleo = float(50)

t1 = float(litros_abastecidos*2.86 + troca_de_oleo)
total = float(t1*(34/100)) + t1

print(round(total,2))