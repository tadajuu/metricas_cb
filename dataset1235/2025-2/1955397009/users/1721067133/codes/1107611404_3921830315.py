litros = float(input("Informe a quantidade de litros abastecidos: "))

vtotal1 = (litros * 2.86) + 50
vtotal = vtotal1 + ((34/100) * vtotal1)

print(round(vtotal,2))