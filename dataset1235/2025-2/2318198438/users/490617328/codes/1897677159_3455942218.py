# Este código é apenas um ESBOÇO da solução.
# Modifique-o para atender as especificações do enunciado.

# Leitura das entradas e conversao para float:
vu = float(input("Qual o valor unitario do jogo? "))
amount = float(input("Qual o valor diposnivel para a aquisicao dos jogos? "))

# Calculo do valor a ser pago, incluindo o frete:
total = vu*8 + 45
saldo = amount - total

# Impressao do valor total e do saldo:
print(round(total,1))
print(round(saldo,1))