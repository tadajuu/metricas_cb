# Amount
gasolina_litros= float(input())

# Adenddum
preço_gasolina= gasolina_litros * 2.86
valor_serviços= preço_gasolina + 50.00
taxa_aumento_icms= valor_serviços * 34/100
valor_total_icms = valor_serviços + taxa_aumento_icms

# As such

print(round(valor_total_icms,2))