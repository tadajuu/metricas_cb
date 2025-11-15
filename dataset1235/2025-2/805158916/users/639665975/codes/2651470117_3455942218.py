# Este código é apenas um ESBOÇO da solução.
# Modifique-o para atender as especificações do enunciado.

# Leitura das entradas e conversao para float:
valor = float(input("Qual o valor unitario do jogo? "))
budget = float(input("Qual o valor disponivel para a aquisicao dos jogos? "))

# Calculo do valor a ser pago, incluindo o frete:
total = valor*8+45
saldo = budget

# Impressao do valor total e do saldo:
print(round(total,1))
print(round(saldo-total,1))

