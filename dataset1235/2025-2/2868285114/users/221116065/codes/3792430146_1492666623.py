suco = int(input("Qual a quantidade de sucos?: "))
salgado = int(input("Qual a quantidade de salgado?: "))
valor_disponivel = float(input("Qual o valor disponivel?: "))

valor_suco = 3.00
valor_salgado = 3.50

calculo_suco = suco * valor_suco
calculo_salgado = salgado * valor_salgado

total = calculo_suco + calculo_salgado

if valor_disponivel >= total:
  print(total)
  print("Sim")

else:
  print(total)
  print("Nao")