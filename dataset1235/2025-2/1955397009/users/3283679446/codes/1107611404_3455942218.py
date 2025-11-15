# Este código é apenas um ESBOÇO da solução.
# Modifique-o para atender as especificações do enunciado.

# Leitura das entradas e conversao para float:
jogo = float(input("Qual o valor unitário do jogo? "))
saldo = float(input("Qual o valor diposnível para a aquisição dos jogos? "))

# Calculo do valor a ser pago, incluindo o frete:
total = 8 * jogo + 45
resto = saldo - total
resto_arrendondado = round(resto, 1)

# Impressao do valor total e do saldo:
print(total)
print(resto_arrendondado)