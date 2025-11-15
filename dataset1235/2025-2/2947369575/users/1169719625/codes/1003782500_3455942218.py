valor_jogo = float(input())

valor_disponivel = float(input())

valor_total = (valor_jogo * 8) + 45.0
valor_restante = valor_disponivel - valor_total

print(round(valor_total, 1))
print(round(valor_restante, 1))