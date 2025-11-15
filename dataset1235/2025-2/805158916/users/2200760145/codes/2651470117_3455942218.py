valor_unitario = float(input())
valor_disponivel = float(input())
preco_total = (8 * valor_unitario) + 45.00
valor_restante = valor_disponivel - preco_total
print(round(preco_total, 1))
print(round(valor_restante, 1))