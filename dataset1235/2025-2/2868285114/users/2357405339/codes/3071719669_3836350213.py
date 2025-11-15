peso_gramas = float(input())
quantidade_em_gramas = float(input())

setedias = quantidade_em_gramas*7
resto = peso_gramas - setedias
print(round(resto,3))