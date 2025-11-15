jogo1 = float(input("Quantos jogos ? "))
pagar = float(input("Qual o valor do jogo ? "))
frente = float(input("Qual o valor do frente ? ")) 
# Calculo do valor a ser pago, incluindo o frete:
total = (jogo1*pagar)+frente

# Impressao do valor total e do saldo:
print(round(total,2))