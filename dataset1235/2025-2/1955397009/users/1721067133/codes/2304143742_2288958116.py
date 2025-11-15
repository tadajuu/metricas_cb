qtd = int(input())
jogo1 = float(input())

if qtd == 1:
  print(jogo1)
else:
  jogo2 = float(input())
  vtotal = jogo1 + jogo2 - (jogo2*0.25)
  print(round(vtotal,2))