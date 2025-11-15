qtd = float(input("Digite a quantidade de litros abastecidos: "))
litro = 2.86
oleo = 50.00
total = (qtd*litro)+oleo
icms = total*(34/100)

print(round(total+icms,2))