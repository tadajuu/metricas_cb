precoGasolina = 2.86
trocaOleo = 50.0

litrosQuantidade = float(input())
total = (precoGasolina * litrosQuantidade) + 50
total = total + (total * 0.34)
print(round(total, 2))