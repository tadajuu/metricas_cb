quantidade = int(input("digite a quantidade de jogos"))
valorunitario = float(input("digite o valor de cada jogo"))
frete         = float(input("digite o valor do frete"))
Total = quantidade * valorunitario + frete
print(round(Total,2))