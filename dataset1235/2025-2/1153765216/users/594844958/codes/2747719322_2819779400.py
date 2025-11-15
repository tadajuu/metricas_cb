quantidade_de_jogos = int(input())
valor_unitario = float(input())
frete = float(input())

total = quantidade_de_jogos * valor_unitario + frete

print(round(total, 2))