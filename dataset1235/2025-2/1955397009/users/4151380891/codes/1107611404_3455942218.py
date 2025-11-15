valorU = float(input("Qual o valor unitario do jogo? "))
valorD = float(input("Qual o valor diposnivel para a aquisicao dos jogos? "))

# Calculo do valor a ser pago, incluindo o frete:
total = (valorU * 8)+ 45
saldo = (valorD - total)

# Impressao do valor total e do saldo:
print(round(total, 1))
print(round(saldo, 1))