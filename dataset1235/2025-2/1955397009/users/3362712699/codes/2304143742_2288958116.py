q = int(input("Quantos jogos você comprou? "))
if q == 1:
  v1 = float(input("Qual o preço?"))
  print(round(v1 * q, 2))
if q == 2:
  v1 = float(input("Qual o preço do primeiro jogo?"))
  v2 = float(input("Qual o preço do segundo jogo?"))
  print(round(v1 + 0.75 * v2, 2))