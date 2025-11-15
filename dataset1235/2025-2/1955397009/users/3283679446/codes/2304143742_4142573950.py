quant = int(input("Informe a quantidade de morangos: "))
preco_12_ou_mais = quant * 1.35
preco_menos_de_12 = quant * 1.50

if quant >= 12:
  print(round(preco_12_ou_mais, 2))

else:
  print(round(preco_menos_de_12, 2))