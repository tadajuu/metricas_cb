# Este código é apenas um ESBOÇO da solução.
# Modifique-o para atender as especificações do enunciado.

# Leitura das entradas e conversao para float:
preco_jogo = float(input(" "))
valor_disponivel = float(input(" "))

# Calculo do valor a ser pago, incluindo o frete:
custo_total = preco_jogo * 8 + 45
saldo = valor_disponivel - custo_total

# Impressao do valor total e do saldo:
print(f"{custo_total:.1f}")
print(f"{saldo:.1f}")