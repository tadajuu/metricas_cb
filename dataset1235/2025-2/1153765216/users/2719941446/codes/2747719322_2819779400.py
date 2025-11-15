qty_jogos=float(input("Digite a quantidade de jogos:"))
valor=float(input("Digite o valor unitário de cada jogo:"))
frete=float(input("Digite o valor do frete:"))

total=qty_jogos*valor+frete

print(round(total,2))