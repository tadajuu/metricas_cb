pesoracao = float(input())
quantdias = float(input())
consumo_5_dias = quantdias * 5
restante = pesoracao - consumo_5_dias
restantearredondado = round(restante, 2)
print(restantearredondado)