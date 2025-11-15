consumo = float(input())

if consumo <= 150.0:
  valor_total = 0.60 * consumo + 5.0

else:
  valor_total = 0.75 * consumo + 16

print(round(valor_total, 2))