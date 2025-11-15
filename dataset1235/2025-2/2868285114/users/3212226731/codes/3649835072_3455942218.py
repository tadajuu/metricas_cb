# Este código é apenas um ESBOÇO da solução.
# Modifique-o para atender as especificações do enunciado.

# Leitura das entradas e conversao para float:
valorUnit = float(input())
valorDisp = float(input())

# Calculo do valor a ser pago, incluindo o frete:
total = valorUnit*8 + 45.00
saldo = valorDisp - total

# Impressao do valor total e do saldo:
print(round(total,1))
print(round(saldo,1))