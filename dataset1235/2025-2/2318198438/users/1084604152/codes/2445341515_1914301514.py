ICMS = 1.31

minutos_por_mes = float(input())

valor_mensal = (0.28 * minutos_por_mes) + 23
valor_total = valor_mensal * ICMS

print(f"{round(valor_total,2)}")