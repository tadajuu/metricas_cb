# Lendo os valores
valor_jogo = float(input())
valor_disponivel = float(input())
# Calculando preço total e restante
preco_total = valor_jogo * 8 + 45
restante = valor_disponivel - preco_total
# Saída arredondada para 1 casa decimal
print(round(preco_total, 1))
print(round(restante, 1))