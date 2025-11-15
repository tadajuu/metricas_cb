# Este código é apenas um ESBOÇO da solução.
# Modifique-o para atender as especificações do enunciado.

# Leitura das entradas e conversao para float:
vu = float(input("Qual o valor unitario do jogo? "))
saldo = float(input("Qual o valor diposnivel para a aquisicao dos jogos? "))

# Calculo do valor a ser pago, incluindo o frete:
total = round(vu*8.0+45.0,1)
saldo = round(saldo - total,1)

# Impressao do valor total e do saldo:
print(total)
print(saldo)