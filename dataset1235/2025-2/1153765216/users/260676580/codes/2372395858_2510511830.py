minuto =  float(input())
plano = 45+(0.97*minuto)
icms = plano * (42/100)
total =  plano + icms

print(round(total,2))