# Este código é apenas um ESBOÇO da solução.
# Modifique-o para atender as especificações do enunciado.

# Leitura das entradas e conversao para float:
x = float(input("Qual o valor unitario do jogo? "))
y = float(input("Qual o valor disponivel para a aquisicao dos jogos? "))

# Calculo do valor a ser pago, incluindo o frete:
total = x*8+45
saldo = y-total

# Impressao do valor total e do saldo:
print(round(total, 1))
print(round(saldo, 1))