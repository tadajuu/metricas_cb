strawberry = int(input("Digite a quantidade de Morangos: "))
if strawberry >= 12:
  valor = 1.35 * strawberry
  print(round(valor, 2))
else:
  valor = 1.50 * strawberry
  print(round(valor, 2))