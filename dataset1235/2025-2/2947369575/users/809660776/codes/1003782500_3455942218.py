valor_jogo = float(input())
dinheiro_disponivel = float(input())

frete = 45.0
quantidade_de_jogos = 8

total_compra = valor_jogo * 8 + frete
dinheiro_restante = dinheiro_disponivel - total_compra

print(round(total_compra, 1))
print(round(dinheiro_restante, 1))