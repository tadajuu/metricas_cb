# Este código é apenas um ESBOÇO da solução.
# Modifique-o para atender as especificações do enunciado.

# Leitura das entradas e conversao para float:
num = float(input("Qual o valor unitario do jogo? "))
dinheiro = float(input("Qual o valor diposnivel para a aquisicao dos jogos? "))

# Calculo do valor a ser pago, incluindo o frete:
total = round((8*num+45),1)
saldo = round((dinheiro-total),1)

# Impressao do valor total e do saldo:
print(total)
print(saldo)