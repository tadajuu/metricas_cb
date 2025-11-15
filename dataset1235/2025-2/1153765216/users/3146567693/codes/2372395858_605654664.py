peso = float(input("digite o peso da  mercadoria em Kg: "))
total = peso * 43,21 + 25,00 
final = total + total * (62/100)
print(round(final,2))