n = int(input())
if n < 12:
 preco = 1.50
else:
 preco = 1.35
total = n * preco
print(round(total, 2))