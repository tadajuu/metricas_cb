tempo = float(input())

total_gasto = tempo * 15 + 5
icms = total_gasto * (20/100)

total_pago = total_gasto + icms

print(round(total_pago,1))