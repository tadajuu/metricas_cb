quantidade = int(input())
valor_unitario = float(input())
valor_frete = float(input())
preco_total = (quantidade * valor_unitario) + valor_frete
print(round(preco_total,2))