# Este código é apenas um ESBOÇO da solução.
# Modifique-o para atender as especificações do enunciado.

# Leitura das entradas e conversao para float:
uni = float(input("Qual o valor unitario do jogo? "))
banco = float(input("Qual o valor diposnivel para a aquisicao dos jogos? "))

# Calculo do valor a ser pago, incluindo o frete:
total = uni*8+45
saldo = banco-total

# Impressao do valor total e do saldo:
print(round((total), 2))
print(round((saldo), 2))