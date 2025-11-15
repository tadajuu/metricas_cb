valor_jogo = float(input())
valor_disponivel = float(input())
frete = 45.0
quantidade = 8
preco_total = quantidade * valor_jogo + frete
restante = valor_disponivel - preco_total
print(f"{preco_total:.1f}")
print(f"{restante:.1f}")