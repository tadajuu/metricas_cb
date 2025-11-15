litros = float(input("Litros abastecidos: "))
gasolina = litros*2.86
vt = gasolina+50
icms = vt*(34/100)
total = vt+icms
print(round(total, 2))