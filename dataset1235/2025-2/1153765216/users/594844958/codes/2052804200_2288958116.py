quantidade_jogos = int(input())
jogo1 = float(input())

if quantidade_jogos == 2:
  jogo2 = float(input())
  valor_total = jogo1 + (jogo2 - (jogo2*(25/100)))
  
  print(round(valor_total, 2))
  
elif quantidade_jogos == 1:
  print(round(jogo1, 2))

  

