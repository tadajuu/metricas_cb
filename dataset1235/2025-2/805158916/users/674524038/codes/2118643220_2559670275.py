peso = float(input("Peso: "))
quantidade = float(input("Quantidade diária: "))
#Quantidade que restará
qt = peso - (quantidade * 7)
print(round(qt, 3))