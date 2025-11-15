quant = float(input("Quantidade de jogos: "))
valor = float(input("Qual o valor unitario do jogo? "))
frete = float(input("Qual o valor do frete? "))

# Calculo do valor a ser pago, incluindo o frete:
total = valor*quant+frete

# Impressao do valor total e do saldo:
print(round(total,1))


