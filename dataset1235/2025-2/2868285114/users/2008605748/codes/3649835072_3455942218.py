preco_jogo = float(input())
dinheiro = float(input())
total = (preco_jogo * 8) + 45
restante = dinheiro - total
print(round(total,1))
print(round(restante,1))