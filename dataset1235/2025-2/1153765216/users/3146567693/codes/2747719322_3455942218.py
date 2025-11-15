# Este código é apenas um ESBOÇO da solução.
# Modifique-o para atender as especificações do enunciado.

# Leitura das entradas e conversao para float:
valor_uni = float(input("Qual o valor unitario do jogo? "))
money = float(input("Qual o valor diposnivel para a aquisicao dos jogos? "))

# Calculo do valor a ser pago, incluindo o frete:
total = valor_uni * 8 + 45.00
saldo = money - total

# Impressao do valor total e do saldo:
print(round(total,1))
print(round(saldo,1))