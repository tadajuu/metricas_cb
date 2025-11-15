quantidade = int(input("Qual a quantidade de jogos?: "))
valor_uni = float(input("Qual o valor unitario do jogo?: "))
frete = float(input("Qual o valor do frete total?: "))

total = (valor_uni * quantidade) + frete

print(total)