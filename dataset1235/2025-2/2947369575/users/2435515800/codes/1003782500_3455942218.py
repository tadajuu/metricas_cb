
valor_unitario = float(input())
valor_disponivel = float(input())
frete = 45.0
valor_total = (valor_unitario * 8) + frete
restante = valor_disponivel - valor_total
print(round(valor_total, 1))
print(round(restante, 1))