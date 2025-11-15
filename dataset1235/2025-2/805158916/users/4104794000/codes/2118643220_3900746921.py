peso = float(input("peso da racao em gramas"))
quantidade = float(input("quantidade de racao em gramas"))

quantidade_final = peso - (7*quantidade)
print(round(quantidade_final,2))