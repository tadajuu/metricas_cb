# Este código é apenas um ESBOÇO da solução.
# Modifique-o para atender as especificações do enunciado.

# Leitura das entradas e conversao para float:
game_price = float(input())
avaiable_money = float(input())

# Calculo do valor a ser pago, incluindo o frete:
total = round(game_price*8+45,1)
saldo = round(avaiable_money-total,1)

# Impressao do valor total e do saldo:
print(total)
print(saldo)