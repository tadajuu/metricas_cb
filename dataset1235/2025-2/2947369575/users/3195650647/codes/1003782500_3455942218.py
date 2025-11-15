# Este código é apenas um ESBOÇO da solução.
# Modifique-o para atender as especificações do enunciado.

# Leitura das entradas e conversao para float:
v1 = float(input("Qual o valor unitario do jogo? "))
v2 = float(input("Qual o valor diposnivel para a aquisicao dos jogos? "))
Q = 8
frete = 45.00
# Calculo do valor a ser pago, incluindo o frete:
total = v1*Q+frete
saldo = v2-total

# Impressao do valor total e do saldo:
print(round(total,1))
print(round(saldo,1))