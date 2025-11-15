quant = int(input())
preco1 = float(input())

if quant == 1:
  total = preco1
else:
  preco2 = float(input())
  total = preco1 + preco2 * 0.75

print(round(total,2))