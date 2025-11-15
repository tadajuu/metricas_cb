# Este código é apenas um ESBOÇO da solução.
# Modifique-o para atender as especificações do enunciado.

# Leitura das entradas e conversao para float:
jogo = float(input("Qual o valor unitario do jogo? "))
vdisp = float(input("Qual que voce tem disponivel "))

# Calculo do valor a ser pago, incluindo o frete:
total = (jogo*8) +45
saldo = vdisp - total
total = round(total, 2)
saldo = round(saldo, 2)
# Impressao do valor total e do saldo:
print(total)
print(saldo)