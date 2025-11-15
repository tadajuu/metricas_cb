#Quantidade de jogos
qj = int(input("Quantidade de jogos a serem encomendados: "))
#Valor unitário de cada jogo
vu = float(input("O valor unitário de cada jogo: "))
#Valor do frete
vf = float(input("Valor do frete: "))
#Soma dos valores
total = (qj * vu) + vf
#Impressão do total
print("Total: ",round(total, 2))