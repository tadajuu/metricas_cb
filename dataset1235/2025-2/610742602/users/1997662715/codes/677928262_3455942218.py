valor_jogo = float(input())
valor_disponivel = float(input())

total_compra = (valor_jogo * 8 ) + 45
resto_dinheiro = valor_disponivel - total_compra

print(round(total_compra, 1))
print(round(resto_dinheiro, 1))