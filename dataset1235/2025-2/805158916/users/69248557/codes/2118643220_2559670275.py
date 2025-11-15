peso = float(input("Digite o peso do saco da ração em gramas "))
quantidade = float(input("Digite a quantidade diaria "))


total = peso - quantidade * 7

print(round(total, 3))
