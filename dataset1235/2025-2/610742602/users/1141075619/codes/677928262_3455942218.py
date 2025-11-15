

VJ = float(input("Qual o valor unitario do jogo? "))
VD = float(input("Qual o valor diposnivel para a aquisicao dos jogos? "))

total = VJ * 8 + 45
saldo = VD - total

print(round (total,1))
print(round (saldo,1))