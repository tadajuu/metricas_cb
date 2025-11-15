# Este código é apenas um ESBOÇO da solução.
# Modifique-o para atender as especificações do enunciado.

# Leitura das entradas e conversao para float:
pjogo = float(input("Valor do jogo: "))
vlrdspl = float(input("Valor diposnivel: "))

# Calculo do valor a ser pago, incluindo o frete:
total = pjogo*8+45
saldo = vlrdspl-total

# Impressao do valor total e do saldo:
print(round(total,1))
print(round(saldo,1))