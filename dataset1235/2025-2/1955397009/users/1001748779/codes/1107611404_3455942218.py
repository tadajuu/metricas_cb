# Este código é apenas um ESBOÇO da solução.
# Modifique-o para atender as especificações do enunciado.

# Leitura das entradas e conversao para float:
VJ = float(input("Qual o valor unitario do jogo? "))
VD = float(input("Qual o valor diposnivel para a aquisicao dos jogos? "))

# Calculo do valor a ser pago, incluindo o frete:
total = (VJ * 8 + 45.00)
saldo = (VD - total)

# Impressao do valor total e do saldo:
print(round(total, 2))
print(round(saldo, 2))