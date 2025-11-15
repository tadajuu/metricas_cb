qtd = int(input().strip())
valor_unit = float(input().strip().replace(',',','))
frete = float(input().strip().replace(',',','))

total = qtd * valor_unit + frete
print(f'{total:.1f}')