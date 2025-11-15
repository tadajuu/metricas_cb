jogos = int(input("Insira um numero de jogos:"))
preço = float(input("Insira o valor dos jogos:"))
frete = float(input("Insira o valor do frete:"))

Q1 = jogos * preço
Q2 = Q1 + frete

print(Q2)