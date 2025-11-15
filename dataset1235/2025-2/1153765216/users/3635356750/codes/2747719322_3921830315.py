litros = float(input())
valor_gasolina = litros * 2.86
subtotal = valor_gasolina + 50.00
icms = subtotal * 0.34
total = subtotal + icms
print(f"{total:.2f}")