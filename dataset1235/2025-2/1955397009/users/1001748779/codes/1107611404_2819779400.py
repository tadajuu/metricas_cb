#Quantidade de jogos; valores dos jogos e do frete
Qu = int(input("qual a quantidade de jogos a serem encomendados?"))
Va = float(input("qual o valor unitario de cada jogo?"))
Fr = float(input("qual o valor do frete?"))

#Preco total a ser pago por Estanislau
total = (Qu * Va + Fr)

#Impressao do valor total
print(total)