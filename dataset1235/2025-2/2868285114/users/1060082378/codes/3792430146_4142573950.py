valor_morango = int(input())
valor_com_desconto = int(input())
quantidade = int(input("digite uma quantidade: "))
if quantidade >=12:
  print(quantidade * valor_com_desconto)
else:
  print(round(quantidade * valor_morango, 2))