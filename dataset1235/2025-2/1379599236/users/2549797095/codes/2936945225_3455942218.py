pj=float(input())
dinheiro = float(input())
frete = 45.0
quantidade = 8
preço_total = (pj*quantidade) + frete
resto= dinheiro - preço_total
preço_total = round(preço_total,1)
resto = round(resto,1)
print(preço_total)
print(resto)
