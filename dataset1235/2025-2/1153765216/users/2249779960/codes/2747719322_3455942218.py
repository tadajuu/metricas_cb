valor_unitario = float(input())
valor_disponivel = float(input())

frete = 45.0
preco_total = (8 * valor_unitario) + frete
restante = valor_disponivel - preco_total

print(round(preco_total, 1))
print(round(restante, 1))