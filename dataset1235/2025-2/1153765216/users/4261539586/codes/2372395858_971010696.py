peso = float(input("digite um valor de peso em gramas: "))
quantidade = float(input("digite a qtd diaria em gramas: "))

qtd = (peso - quantidade) - 5
print(round(qtd, 3))