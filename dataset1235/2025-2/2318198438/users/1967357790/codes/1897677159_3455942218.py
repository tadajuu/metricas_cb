# Este código é apenas um ESBOÇO da solução.
# Modifique-o para atender as especificações do enunciado.

# Leitura das entradas e conversao para float:
valor_unitario = float(input("Qual o valor unitario do jogo?"))
valor_disponivel = float(input("Qual o valor diposnivel para a aquisicao dos jogos?"))

# Calculo do valor a ser pago, incluindo o frete:
frete = 45.0
jogos = 8
total = (valor_unitario * jogos) + frete
saldo = valor_disponivel - total

# Impressao do valor total e do saldo:
print(total)
print(saldo)