qtd_morangos = int(input())

if qtd_morangos >= 12:
  preco = qtd_morangos * 1.35
else:
  preco = qtd_morangos * 1.50
print(round(preco,2))