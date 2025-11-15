# Este código é apenas um ESBOÇO da solução.
# Modifique-o para atender as especificações do enunciado.

# Leitura das entradas e conversao para float:
Valor1 = float(input("Qual o valor unitario do jogo? "))
Valor2 = float(input("Qual o valor diposnivel para a aquisicao dos jogos? :"))

# Calculo do valor a ser pago, incluindo o frete:
total= 8*Valor1+45
saldo= Valor2-total

# Impressao do valor total e do saldo:
print(round(total ,1))
print(round(saldo , 1))