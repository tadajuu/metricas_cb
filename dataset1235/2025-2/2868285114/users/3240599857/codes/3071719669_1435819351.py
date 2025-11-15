peso_gramas = float(input())
quant_diaria_gramas = float(input())
cincodias = quant_diaria_gramas*5
resto = peso_gramas - cincodias
print(round(resto,2))