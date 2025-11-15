x = float(input("Qual o valor unitario do jogo? "))
y = float(input("Qual o valor diposnivel para a aquisicao dos jogos? "))


total = (8*x+45)
saldo = y-total

print(round(total,1))
print(round(saldo,1))