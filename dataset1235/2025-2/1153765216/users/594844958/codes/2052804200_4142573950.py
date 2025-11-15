quantidade = int(input())

if quantidade < 12:
  valor = 1.50 * quantidade

else:
  valor = 1.35 * quantidade

print(round(valor, 2))