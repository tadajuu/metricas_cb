# Entrada

quantidade_jogos = float(input("Qual a quantidade de jogos a serem comprados?"))
valor_unitario = float(input("Qual o valor unitario de cada jogo"))
valor_frete = float(input("Qual o valor do frete"))

total_jogos = quantidade_jogos * valor_unitario
total_frete = total_jogos + valor_frete

# Saída
print(total_frete)