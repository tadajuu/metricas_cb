quantidade_jogos = int(input())
valor_unitario = float(input())
frete = float(input())

preco_total = (valor_unitario*quantidade_jogos) + frete

print(round(preco_total,1))