qtd_litros = float(input())
preco_litros = qtd_litros * 2.86
taxa = (preco_litros + 50)* 0.34

total = preco_litros + 50 + taxa
print(round(total,2))