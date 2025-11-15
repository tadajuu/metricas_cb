weight = float(input("O peso do saco de ração (em gramas):"))
quant = float(input("Quantidade diária de ração em gramas:"))

leftovers = weight-(7*quant)


print(round(leftovers,3))