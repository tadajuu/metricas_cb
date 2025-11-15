preco_unitario = float(input())
valor_disponivel = float(input())
total = (8 * preco_unitario) + 45
restante = valor_disponivel - total
print(round(total, 1))
print(round(restante, 1))