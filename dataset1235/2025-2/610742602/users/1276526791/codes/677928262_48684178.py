# Lendo o total de vendas 
total_vendas = float(input())
# Calculando o lucro (30% das vendas)
lucro = total_vendas * (30 / 100)
# Imprimindo o lucro arredondado para 2 casas decimais
print(round(lucro, 2))