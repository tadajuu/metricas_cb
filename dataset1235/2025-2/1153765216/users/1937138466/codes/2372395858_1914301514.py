consumo = float(input("Informe um valor: "))
assinatura =  (0.28 * consumo) + 23
total = assinatura + assinatura * (31/100)
print(round(total, 2))