litragem = float(input("Quantos litros vc abasteceu: "))
servico = (litragem * 2.86) + 50
total = servico + (servico * (34/100))

print (round(total,2))