peso_racao = float(input("Informe o peso do saco de ração em gramas: "))
quant_diaria = float(input("Informe a quantidade diária: "))

resto = peso_racao - quant_diaria * 4

resto_arredondado = round(resto, 2)

print(resto_arredondado)