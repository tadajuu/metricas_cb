quantidade = int(input())
jogo1 = float(input("Valor jogo1:"))

if (quantidade == 2):
  jogo2 = float(input("Valor jogo2:"))
  total = jogo1 + (jogo2- 0.25*jogo2)
else: 
  total = jogo1

print(round(total,2))