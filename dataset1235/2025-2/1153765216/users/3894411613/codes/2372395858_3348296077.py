tempo = int(input("Tempo em horas: "))

taxa = 15.00
taxa_estac = 5.00

total = (tempo * taxa) + taxa_estac 
porcento_icms = total * (20/100)
total_gasto = total + porcento_icms
print(round(total_gasto , 2))