quantidade = int(input("Digite o numero de morangos comprados: "))
if quantidade < 12:
  preco_unitario = 1.50
else:
  preco_unitario = 1.35
total = quantidade * preco_unitario
total_arredondado = round(total, 2)
print(total_arredondado)