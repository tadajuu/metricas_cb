



jogo = float(input("Qual o valor unitario do jogo?"))
money = float(input("Qual o valor diposnivel para a aquisicao dos jogos? "))


total = jogo*8 + 45
saldo = money - total


print(round(total,2))
print(round(saldo,2))