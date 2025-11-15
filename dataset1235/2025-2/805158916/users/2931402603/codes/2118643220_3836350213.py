psr = float(input("peso do saco de ração em gramas: "))
qrd = float(input("quantidade diária de ração em gramas: "))

qr = psr - (7 * qrd)

print(round(qr, 3))