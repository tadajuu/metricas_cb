Peso = float(input("Peso em gramas"))
Qtd = float(input("Qtd. Diária em gramas"))

fdo = float(Qtd * 5)
Qtdres = (float(round(Peso - fdo,2)))

print (float(round(Qtdres,2)))