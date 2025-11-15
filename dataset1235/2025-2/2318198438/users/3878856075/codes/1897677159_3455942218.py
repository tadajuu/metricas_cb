# Este código é apenas um ESBOÇO da solução.
# Modifique-o para atender as especificações do enunciado.

# Leitura das entradas e conversao para float:
unita= float(input("Qual o valor unitario do jogo?"))
valor= float(input("Qual o valor disponivel para a aquisicao dos jogos?"))

# Calculo do valor a ser pago, incluindo o frete:
total = (8*unita+45.00)
saldo = (valor-total)

# Impressao do valor total e do saldo:
print(round(total, 1))
print(round(saldo, 1))
