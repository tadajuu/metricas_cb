gasolina = float(input("quantidade de litros de gasolina:"))
valor = 2.86 * gasolina + 50
imposto = round(valor * 0.34, 2)
total = valor + imposto
print(round(total, 2))
