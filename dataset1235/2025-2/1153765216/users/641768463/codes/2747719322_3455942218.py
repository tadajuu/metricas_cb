# Este código é apenas um ESBOÇO da solução.
# Modifique-o para atender as especificações do enunciado.

# Leitura das entradas e conversao para float:
VG = float(input("Qual o valor unitario do jogo? "))
Disponivel = float(input("Qual o valor diposnivel para a aquisicao dos jogos? "))

# Calculo do valor a ser pago, incluindo o frete:
total = VG*8+45
saldo = Disponivel - total

# Impressao do valor total e do saldo:
print(round(total, 1))
print(round(saldo, 1))