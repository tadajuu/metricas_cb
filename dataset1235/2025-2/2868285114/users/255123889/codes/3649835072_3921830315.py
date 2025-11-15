litros = float(input(""))
valor_abastecido = (litros)*2.86 + 50
icms = valor_abastecido*34/100
valor_total = valor_abastecido + icms

print(round(valor_total,2))