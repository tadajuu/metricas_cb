# Este código é apenas um ESBOÇO da solução.
# Modifique-o para atender as especificações do enunciado.

# Leitura das entradas e conversao para float:
valor1 = float(input("Qual o valor unitario do jogo? "))
valor2 = float(input("Qual o valor diposnivel para a aquisicao dos jogos? "))

# Calculo do valor a ser pago, incluindo o frete:
total = valor1*8+45
saldo = valor2-total

# Impressao do valor total e do saldo:
print (total)
print (saldo)