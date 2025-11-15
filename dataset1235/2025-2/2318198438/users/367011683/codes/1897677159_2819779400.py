quantidade = int(input())
valor_jogo = float(input())
frete = float(input())
preco_total = quantidade * valor_jogo + frete
print(f"{preco_total:.1f}")