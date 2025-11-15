valor_unitario = float(input())
valor_disponivel = float(input())
total = valor_unitario * 8 + 45 
restante = valor_disponivel - total
print(round(total, 1))
print(round(restante, 1))