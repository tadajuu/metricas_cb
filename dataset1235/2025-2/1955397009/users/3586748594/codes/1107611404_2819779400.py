quantidade = int(input())
valor_unitario = float(input())
frete = float(input())
preco_total = (quantidade * valor_unitario) + frete

print(round(preco_total, 2))