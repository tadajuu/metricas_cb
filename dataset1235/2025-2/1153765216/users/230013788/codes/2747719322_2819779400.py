qe = int(input("Quantidade de jogos a serem encomendados: "))
vu = float(input("Qual valor unitario de cada jogo: "))
vf = float(input("valor do frete: "))

ptotal = (vu*qe) + vf
print(round(ptotal , 1))