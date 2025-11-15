# Lendo a quantidade de jogos (inteiro)
quantidade_jogos = int(input())
#Lendo o valor unitário de cada jogo (float)
valor_jogo = float(input())
# Lendo o valor do frete (float)
frete = float(input())
# Calculando o preço total 
preco_total = (quantidade_jogos * valor_jogo) + frete
#Imprimindo o preço total
print(round(preco_total, 1))