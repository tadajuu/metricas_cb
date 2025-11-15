kwh = float(input("digite um valor: "))

formula = (0.43 * kwh) + 10
total = formula + formula*(25/100)

print(round(total, 2))