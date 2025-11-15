# Este código é apenas um ESBOÇO da solução.
# Modifique-o para atender as especificações do enunciado.

# Leitura das entradas e conversao para float:
X = float(input("qual o valor unitario do jogo?" ))
Y = float(input("qual o valor disponivel para aquisicao dos jogos? "))

# Calculo do valor a ser pago, incluindo o frete:
total = X*8+45.00
saldo = Y%total

# Impressao do valor total e do saldo:
print(round(total,1))
print(round(saldo,1))