# Leitura das entradas e conversao para float:
valor_unit = float(input("Qual o valor unitario do jogo? "))
valor_dispo = float(input("Qual o valor disponivel para a aquisicao dos jogos? "))

# Calculo do valor a ser pago, incluindo o frete:
total = (valor_unit*8) + 45
saldo = valor_dispo - total

# Impressao do valor total e do saldo:
print (round(total, 1))
print (round(saldo, 1))