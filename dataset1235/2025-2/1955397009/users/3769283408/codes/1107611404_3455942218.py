valor_unitario = float(input())
dinheiro_disponivel = float(input())
quantidade=8
frete = 45.0
total = ( quantidade*valor_unitario)+frete
restante = dinheiro_disponivel-total
print(round(total,2))
print(round(restante,2))