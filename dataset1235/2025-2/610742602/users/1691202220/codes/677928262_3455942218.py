# Lê o valor unitário do jogo
valor_unitario = float(input())

# Lê o valor disponível para a compra 
valor_disponivel = float(input())

# Cálculo do valor total (8 jogos + frete de 45.0)
total = (valor_unitario * 8) + 45.0

# Cálculo do saldo
saldo = valor_disponivel - total

# Impressão arredondadada com 1 casa decimal
print(round(total, 1))
print(round(saldo, 1))