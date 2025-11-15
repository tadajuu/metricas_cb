peso = float(input())
qtd_diaria = float(input())
qtd_semanal = qtd_diaria * 4
resto = peso - qtd_semanal
print(round(resto,2))