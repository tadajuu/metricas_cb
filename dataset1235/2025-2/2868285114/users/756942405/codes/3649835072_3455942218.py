# Este código é apenas um ESBOÇO da solução.
# Modifique-o para atender as especificações do enunciado.

# Leitura das entradas e conversao para float:
jogo = float(input("Qual o valor unitario do jogo?: "))
grana = float(input("Qual o valor disponivel para a aquisicao dos jogos?: "))

# Calculo do valor a ser pago, incluindo o frete:
total = (jogo * 8) + 45
saldo = grana - total

# Impressao do valor total e do saldo:
print(round(total, 1))
print(round(saldo, 1))