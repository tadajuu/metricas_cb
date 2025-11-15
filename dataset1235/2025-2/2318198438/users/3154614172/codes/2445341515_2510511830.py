minutos_excedentes = float(input())

valor_a_ser_pago_pelos_minutos = minutos_excedentes * 0.97
plano = 45
t = plano + valor_a_ser_pago_pelos_minutos
icms = t * (42/100)
total_a_ser_pago = t + icms

print(round(total_a_ser_pago,2))