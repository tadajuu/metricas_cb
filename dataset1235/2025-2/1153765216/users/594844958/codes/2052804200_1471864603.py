area = float(input())

if area <= 10000:
  valor_total = area * 5.0
else:
  area_a_mais = area - 10000
  valor_total = (10000 * 5) + (4 * area_a_mais)

print(round(valor_total, 2))