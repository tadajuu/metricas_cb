litros = float(input())
gasolina = litros*2.86
oleo = 50.00
icms = (gasolina + oleo)*(34/100)
total = gasolina + oleo + icms
print(round(total,2))