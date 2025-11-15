# Este código é apenas um ESBOÇO da solução.
# Modifique-o para atender as especificações do enunciado.

# Leitura das entradas e conversao para float:
jogo = float(input("Qual o valor unitario do jogo? "))
valor = float(input("Qual o valor diposnivel para a aquisicao dos jogos? "))

# Calculo do valor a ser pago, incluindo o frete:
total = ((jogo*8)+45)
saldo = (valor)

# Impressao do valor total e do saldo:
print(total)
print(round((saldo-total),1))