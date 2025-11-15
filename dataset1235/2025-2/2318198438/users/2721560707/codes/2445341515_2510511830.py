
minuto = float(input())
valor_exced_mes = 45 + (minuto* 0.97)
valor = valor_exced_mes + (valor_exced_mes *(42/100))
print(round(valor, 2))