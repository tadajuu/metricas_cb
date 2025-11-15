preço = float(input())
dinheiro = float(input())
total = preço * 8 + 45
saldo = dinheiro - total
print(round(total, 2))
print(round(saldo, 2))