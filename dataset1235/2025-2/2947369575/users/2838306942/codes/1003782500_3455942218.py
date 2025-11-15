# Este código é apenas um ESBOÇO da solução.
# Modifique-o para atender as especificações do enunciado.

# Leitura das entradas e conversao para float:
preço_jogo = float(input("Qual o valor unitario do jogo? "))
dinheiro_disponivel = float(input("Qual o valor diposnivel para a aquisicao dos jogos? "))

# Calculo do valor a ser pago, incluindo o frete:
quantidade_de_jogos = 8
frete = 45
custo_total = (preço_jogo * quantidade_de_jogos) + frete
dinheiro_restante = dinheiro_disponivel - custo_total



# Impressao do valor total e do saldo:
print(round(custo_total,1))
print(round(dinheiro_restante,1))