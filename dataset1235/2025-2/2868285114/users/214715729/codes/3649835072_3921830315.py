litros = float(input(""))
valor_abastc = (litros)*2.86 + 50
icms = valor_abastc*34/100
valor_total = valor_abastc + icms

print(round(valor_total,2))