peso = float(input())
qtd_diaria = float(input())
qtd_semana = qtd_diaria*7
sobra = round(peso - qtd_semana, 2)

print(sobra)