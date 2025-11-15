quant = int(input("Quantos jogos deseja comprar? (1/2)"))

if quant == 1:
  jogo1 = float(input("Informe o valor do jogo: "))
  print("Total",jogo1)
elif quant == 2:
  jogo0 = float(input("Informe o valor do jogo 1: "))
  jogo2 = float(input("Informe o valor do jogo 2: "))
  total = jogo0 + jogo2 * 0.75
  print(round(total, 2))
else:
  print("Informe as informações novamente")
  