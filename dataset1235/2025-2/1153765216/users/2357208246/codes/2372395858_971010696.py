#tudo em gramas
peso_saco = float(input())
qtd_racao = float(input())

total_racao_consumida = qtd_racao * 5

racao_restante = peso_saco - total_racao_consumida

print(round(racao_restante, 3))