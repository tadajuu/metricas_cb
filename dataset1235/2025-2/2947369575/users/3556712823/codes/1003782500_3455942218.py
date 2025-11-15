jogo = float(input("Qual o valor unitario do jogo? "))
valor = float(input("Qual o valor disponivel para a aquisicao dos jogos? "))

# Calculo do valor a ser pago, incluindo o frete:
total = float((jogo*8)+ 45.00)
saldo = float(valor - total)

# Impressao do valor total e do saldo:
print(round(total,1))
print(round (saldo,1))