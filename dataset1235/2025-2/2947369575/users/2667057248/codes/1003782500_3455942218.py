# Este código é apenas um ESBOÇO da solução.
# Modifique-o para atender as especificações do enunciado.

# Leitura das entradas e conversao para float:
Valor_jogo = float(input("Qual o valor unitario do jogo? "))
valor_dsponivel = float(input("Qual o valor diposnivel para a aquisicao dos jogos? "))

# Calculo do valor a ser pago, incluindo o frete:
total = (Valor_jogo * 8 ) + 45 
saldo = valor_dsponivel - total

# Impressao do valor total e do saldo:
print(f"{total:.1f}")
print(f"{saldo:.1f}")