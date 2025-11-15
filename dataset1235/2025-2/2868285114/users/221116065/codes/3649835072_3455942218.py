jogo = float(input("Qual o valor unitario do jogo? "))
disponivel = float(input("Qual o valor diposnivel para a aquisicao dos jogos? "))

# Calculo do valor a ser pago, incluindo o frete:
total = jogo * 8 + 45
saldo = disponivel - total

# Impressao do valor total e do saldo:
print(round(total, 1))
print(round(saldo, 1))