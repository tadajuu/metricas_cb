# Este código é apenas um ESBOÇO da solução.
# Modifique-o para atender as especificações do enunciado.

# Leitura das entradas e conversao para float:
valor_unitario = float(input("35"))
valor_disponivel = float(input("400"))

# Calculo do valor a ser pago, incluindo o frete:
total = (8 * valor_unitario) + 45
saldo = (valor_disponivel - total)

# Impressao do valor total e do saldo:
print(round(total, 1))
print(round(saldo, 1))