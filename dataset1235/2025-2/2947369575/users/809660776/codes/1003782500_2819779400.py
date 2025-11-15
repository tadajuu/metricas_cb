quantidade = int(input("quantidade de jogos: "))
valor_jogo = float(input("valor unitário do jogo: "))
frete = float(input( "valor do frete: "))
total = quantidade * valor_jogo + frete

print(round(total,  1))