qtd = int(input("Quantidade de morango: "))
if qtd < 12:
  qtd_arredondado = qtd * 1.5
  print(round(qtd_arredondado,2))
else:
  qtd_arredondado1 = qtd * 1.35
  print(round(qtd_arredondado1,2))
