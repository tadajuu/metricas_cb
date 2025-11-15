quantidade = int(input(""))
valor_unitario = float(input(""))
frete = float(input(""))
valor_total = (quantidade * valor_unitario) + frete
print(round(valor_total, 1))