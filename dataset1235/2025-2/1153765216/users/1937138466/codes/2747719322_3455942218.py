valor_unitario = float(input("Qual o valor unitario de cada jogo?: "))
valor_disponivel = float(input("Qual o valor disponivel para a aquisição dos jogos?: "))

total = (8 * valor_unitario) + 45
saldo = valor_disponivel - total

print(round(total, 1))
print(round(saldo, 1))