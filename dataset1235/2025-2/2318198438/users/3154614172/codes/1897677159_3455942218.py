# Leitura das entradas e conversao para float:
valor_unitario = float(input("Qual o valor unitario do jogo? "))
saldo_disponivel = float(input("Qual o valor diposnivel para a aquisicao dos jogos? "))

# Calculo do valor a ser pago, incluindo o frete:
total = valor_unitario*8 + 45
saldo = saldo_disponivel - total

# Impressao do valor total e do saldo:
print(round(total,1))
print(round(saldo,1))