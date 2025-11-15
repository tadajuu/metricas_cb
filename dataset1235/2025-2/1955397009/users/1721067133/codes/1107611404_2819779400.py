qtd_jogos_encomendados = float(input("Informe a quantidade de jogos a serem encomendados: "))
vunitario = float(input("Informe o valor unitário de cada jogo: "))
frete = float(input("Informe o frete do site: "))

total = (qtd_jogos_encomendados * vunitario) + frete

print(total)