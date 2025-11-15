valor = float(input(print("Qual o valor unitario do jogo? ")))
disponivel = float(input(print("Qual o valor diposnivel para a aquisicao dos jogos? ")))
total = (valor * 8) + 45
saldo = disponivel - total
print(round(total, 1))
print(round(saldo, 1))