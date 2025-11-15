PSR = float(input("Peso do saco de ração em gramas: "))
QPD = float(input("Quantidade diária de ração: "))

QQR = PSR - (4*QPD)

print(round(QQR, 2))