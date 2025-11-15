peso = float(input("Peso do saco de ração em gramas: "))
qtd = float(input("Quantidade diaria de racao em gramas: "))
resto = peso-(qtd*5)

print(round(resto,3))