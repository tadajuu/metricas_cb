
x1= float(input("Qual o valor unitario do jogo? "))
x2= float(input("Qual o valor diposnivel para a aquisicao dos jogos? "))

# Calculo do valor a ser pago, incluindo o frete:
total = (x1*8)+45
saldo = x2-total

# Impressao do valor total e do saldo:
print(round(total,1))
print(round(saldo,1))