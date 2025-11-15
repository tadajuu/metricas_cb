# Este código é apenas um ESBOÇO da solução.
# Modifique-o para atender as especificações do enunciado.

# Leitura das entradas e conversao para float:
valor_unitario = float(input("Qual o valor unitario do jogo?"))
valor_que_tenho = float(input("Qual o valor diponivel para a aquisicao dos jogos? "))

# Calculo do valor a ser pago, incluindo o frete:
total = (valor_unitario * 8) + 45
saldo = valor_que_tenho - total

# Impressao do valor total e do saldo:
print(round(total, 1))
print(round(saldo, 1))