qtd = float(input("Digite a quantidade de jogos: "))
valor = float(input("Digite o valor de cada jogo: "))
frete = float(input("Digite o valor do frete: "))

site = ((qtd*valor)+frete)
print(round(site,2))