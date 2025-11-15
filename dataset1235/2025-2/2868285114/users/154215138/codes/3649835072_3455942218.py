# Este código é apenas um ESBOÇO da solução.
# Modifique-o para atender as especificações do enunciado.

# Leitura das entradas e conversao para float:
valor_unitário = float(input("Qual o valor unitario do jogo? "))
valor_disponível = float(input("Qual o valor diposnivel para a aquisicao dos jogos? "))

# Calculo do valor a ser pago, incluindo o frete:
total = valor_unitário * 8
saldo = total + 45
troco = valor_disponível - saldo
saldo_arredondamento = round(saldo, 1)
troco_arredondamento = round(troco, 1)
# Impressao do valor total e do saldo:
print(saldo_arredondamento)
print(troco_arredondamento)