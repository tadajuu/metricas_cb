
x1 = float(input("Qual o valor unitario do jogo? "))
x2 = float(input("Qual o valor diposnivel para a aquisicao dos jogos? "))

total = (x1*8)+45
saldo = x2-total

print(round(total,1))
print(round(saldo,1))