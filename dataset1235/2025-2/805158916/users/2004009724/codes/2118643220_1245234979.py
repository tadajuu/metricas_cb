PSR = float(input("Peso do saco de racao em gramas"))
QPD = float(input("Quantidade diaria de racao em gramas"))

QQR = PSR - (5*QPD)

print(round(QQR, 2))