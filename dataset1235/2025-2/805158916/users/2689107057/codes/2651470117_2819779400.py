quantidade = int(input("Quantidade de jogos: "))
preco_unitario = float(input("Preço unitário do jogo: "))
frete = float(input("Valor de frete: "))
total = (quantidade * preco_unitario) + frete
print(total)