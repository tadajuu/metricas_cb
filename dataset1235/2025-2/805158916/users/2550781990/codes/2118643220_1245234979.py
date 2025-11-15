peso = float(input("Peso do saco em gramas: "))
diaria = float(input("Quantidade de ração em gramas: "))
resto = peso - (diaria * 5)
print(round(resto,2))