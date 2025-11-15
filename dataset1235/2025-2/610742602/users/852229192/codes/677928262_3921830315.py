litros_abastecidos = float(input())
preco = litros_abastecidos * 2.86 + 50
servico = preco * (34/100)
total = preco + servico
print(round(total,2))
