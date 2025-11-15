q_jogos = int(input("Quantos jogos a serem encomedados?"))
valorU = float(input("Qual o preço do jogo?"))
frete = float(input("qual o valor do frete?"))

preco_total = (q_jogos * valorU) + frete
print(preco_total)