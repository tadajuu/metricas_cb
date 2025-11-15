
r = float(input("Qual o valor unitario do jogo? "))
s = float(input("Qual o valor diposnivel para a aquisicao dos jogos? "))

total = r * 8 + 45
saldo = s - (total)

print(round(total, 1))
print(round(saldo, 1))

