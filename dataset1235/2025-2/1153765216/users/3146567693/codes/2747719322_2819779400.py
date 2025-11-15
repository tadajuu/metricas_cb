quantidade = int(input("digite quantos jogos deseja: "))
valor_uni = float(input("digite o valor dos jogos: "))
frete = float(input("valor do frete: "))

preço_ttl = quantidade * valor_uni + frete
print(f"{preço_ttl}")