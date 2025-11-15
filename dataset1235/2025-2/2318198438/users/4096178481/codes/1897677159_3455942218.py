valor_pago = float(input("Valor pago: "))
valor_disponivel = float(input("Valor disponivel: "))
gasto = valor_pago*8 + 45
print(round(gasto,1))
print(round(valor_disponivel - (gasto),1))