valor = float(input("Insira o valor do jogo:"))
dinheiro = float(input("Insira o valor disponivel para comprar os jogos:"))

Q1 = valor * 8 + 45
Q2 = dinheiro - Q1

print(round(Q1,1))
print(round(Q2,1))