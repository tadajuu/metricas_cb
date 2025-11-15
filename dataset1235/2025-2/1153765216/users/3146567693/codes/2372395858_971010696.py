peso = float(input("digite o peso do saco da ração em grama: "))
quantidade = float(input("Digite a quantidade diária de ração: "))
x = peso - quantidade % 5

print(round(resto,3))