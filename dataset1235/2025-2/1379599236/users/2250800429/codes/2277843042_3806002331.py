litros = float(input())
custo_gasolina = litros*2.86
subtotal = custo_gasolina+50
total = subtotal+ (subtotal*(34/100))
print(round(total,2))
