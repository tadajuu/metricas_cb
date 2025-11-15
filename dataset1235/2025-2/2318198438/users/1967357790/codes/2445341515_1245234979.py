peso = float(input())
qtd_diaria = float(input())

qtd_racao_resto = qtd_diaria * 5

print(round(peso - qtd_racao_resto, 2))