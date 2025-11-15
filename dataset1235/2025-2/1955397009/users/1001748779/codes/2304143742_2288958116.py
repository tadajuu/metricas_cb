quantidade = int(input("quantidade de jogos:"))
jogo1 = float(input("Preço do jogo 1:"))

if quantidade == 2:
  jogo2 = float(input("Preço do jogo 2:"))
  total = jogo1 + (jogo2 - jogo2*(25/100))
else:
  total = jogo1

print(round(total,2))