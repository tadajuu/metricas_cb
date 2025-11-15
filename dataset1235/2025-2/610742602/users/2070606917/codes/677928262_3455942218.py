valor_unitario = float(input())
# Leitura do valor disponivel para compra 
valor_disponivel = float(input())
# Cálculo do valor total (8 jogos + frete de 45.0)
total = (valor_unitario * 8) + 45.0


# Calculo do saldo restante
saldo = valor_disponivel - total

# Impressao arrendondadda com 1 casa decimal
print(round(total, 1))
print(round(saldo, 1 ))