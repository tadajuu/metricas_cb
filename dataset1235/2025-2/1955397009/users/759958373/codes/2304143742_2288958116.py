quant_jogos = int(input())
preco_1 = float(input())

if(quant_jogos == 1):
  print(round(preco_1, 2))
if(quant_jogos == 2):
  preco_2 = float(input())
  total = preco_1 + preco_2*(75/100)
  print(round(total, 2))