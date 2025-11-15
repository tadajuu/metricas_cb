l = float(input("litros abastecidos: "))
v = l*2.86
o = 50.0
s = v+o
icms = s*(34/100)

print(round(s+icms, 2))