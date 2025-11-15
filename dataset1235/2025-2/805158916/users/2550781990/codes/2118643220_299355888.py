aluguel = 50
taxa = 30
icms = 18/100
dias = int(input())
valor = aluguel * dias + taxa
total = valor * (18/100)
varfinal = valor + total
print(round(varfinal,2))