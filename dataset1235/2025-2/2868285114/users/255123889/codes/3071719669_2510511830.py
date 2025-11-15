quantidade = float(input())
minutos = quantidade * 0.97
min = minutos + 45
icms = min * (42/100)
total = min + icms
print(round(total,2))