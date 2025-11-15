peso_gramas = float(input())
quant_diaria_gramas = float(input())

##serao 4 dias, ent precisa descobrir quanto restara em 4 dias 

quatrodias = quant_diaria_gramas*4

resto = peso_gramas - quatrodias

print(round(resto,2))