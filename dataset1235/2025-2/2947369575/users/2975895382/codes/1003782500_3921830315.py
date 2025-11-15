

litroGasolina = 2.86
trocaOleo = 50.00

icms = 0.34

nLitros = float(input("Digite quantos litros foram abastecidos: "))
valorAbastecimento = (nLitros * litroGasolina) + trocaOleo

res = valorAbastecimento  + (valorAbastecimento * icms)

print(round(res,2))