# Este código é apenas um ESBOÇO da solução.
# Modifique-o para atender as especificações do enunciado.

# Leitura das entradas e conversao para flo
valor_uni = float(input(" "))
disponivel = float(input(" "))
# Calculo do valor a ser pago, incluindo o frete:
total = (valor_uni)*8+45
saldo = disponivel - total

# Impressao do valor total e do saldo:
print(round(total,1))
print(round(saldo,1))