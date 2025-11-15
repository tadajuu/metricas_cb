# Este código é apenas um ESBOÇO da solução.
# Modifique-o para atender as especificações do enunciado.

# Leitura das entradas e conversao para float:
valor_jogo = float(input("Qual o valor unitario do jogo? "))
dinheiro_disponivel = float(input("Qual o valor diposnivel para a aquisicao dos jogos? "))

# Calculo do valor a ser pago, incluindo o frete:
total = (valor_jogo * 8 + 45.00)

saldo = dinheiro_disponivel -  total

# Impressao do valor total e do saldo:
print(f"{total:.1f}")
print(f"{saldo:.1f}")