morango = int(input("Qual a quantidade de morangos?: "))

if morango >= 12:
  custo = 1.35
  valor = custo * morango
  print(round(valor, 2))

else:
  custo = 1.50
  valor = custo * morango
  print(round(valor, 2))