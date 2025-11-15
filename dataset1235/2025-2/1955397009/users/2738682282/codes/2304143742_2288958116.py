quantidade = int(input())
jogo1 = float(input())

if quantidade == 2: 
  jogo2 = float(input())
  total = jogo1 + (jogo2 - 0.25*jogo2)

else: 
  total = jogo1

print(round(total, 2))