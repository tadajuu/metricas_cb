# Leitura das entradas e conversao para float:
vu = float(input("Qual o valor unitario do jogo? "))
va = float(input("Qual o valor diposnivel para a aquisicao dos jogos? "))

# Calculo do valor a ser pago, incluindo o frete:
total = (vu*8 )+ 45.00
saldo =  va - total

# Impressao do valor total e do saldo:
print(round(total , 2))
print(round(saldo , 2))