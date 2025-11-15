# Este código é apenas um ESBOÇO da solução.
# Modifique-o para atender as especificações do enunciado.

# Leitura das entradas e conversao para float:
x = float(input())
y = float(input())

# Calculo do valor a ser pago, incluindo o frete:
final = x*8 + 45
resto = y - final 

# Impressao do valor total e do saldo:
print(round(final,1))
print(round(resto,1))