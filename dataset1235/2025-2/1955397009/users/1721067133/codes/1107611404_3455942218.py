# Leitura das entradas e conversao para float:
vunit = float(input("Qual o valor unitario do jogo? "))
vdisp = float(input("Qual o valor diponivel para a aquisicao dos jogos? "))

# Calculo do valor a ser pago, incluindo o frete:
tot = (vunit * 8 ) + 45.0
sald = vdisp - tot

# Impressao do valor total e do saldo:
print(round(tot,1) )
print(round(sald,1) )