# Leitura das entradas e conversao para float:
quant_jogos = int(input("Quantidade de jogos: "))
valor_unit = float(input("Qual o valor unitario do jogo? "))
valor_frete = float(input("Valor do frete: "))

# Calculo do valor a ser pago, incluindo o frete:
total = (valor_unit * quant_jogos) + valor_frete

# Impressao do valor total e do saldo:
print (round(total, 1))