num_jogos = int(input())
vu = float(input())
frete = float(input())

# Calculo do valor a ser pago, incluindo o frete:
total = num_jogos*vu + frete

# Impressao do valor total e do saldo:
print(round(total,1))
