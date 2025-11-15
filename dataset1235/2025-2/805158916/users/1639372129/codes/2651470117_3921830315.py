lit = float(input("quantidade de litros abastecidos: "))
vt = lit * 2.86 + 50
vp = vt*(34/100) + vt
print(round(vp, 2))