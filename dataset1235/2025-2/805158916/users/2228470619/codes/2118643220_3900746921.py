peso = float(input("Digite o peso do saco em gramas: "))
quant = float(input("Digite a quantidade diária de ração: "))
resto = peso - (quant*7)
print("Quantidade que restará depois de uma semana: ",round(resto,2))