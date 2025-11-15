# Este código é apenas um ESBOÇO da solução.
# Modifique-o para atender as especificações do enunciado.

# Leitura das entradas e conversao para float:
richard = float(input())
karla = float(input())

# Calculo do valor a ser pago, incluindo o frete:
total = richard * 8 + 45
saldo = karla - (richard * 8 + 45)

# Impressao do valor total e do saldo:
print(round(total, 1))
print(round(saldo, 1))