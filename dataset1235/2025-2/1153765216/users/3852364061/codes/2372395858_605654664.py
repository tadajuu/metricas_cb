#Informações Iniciais
peso_mercadoria = float(input())

# Calculo da Taxa
preco_parcial = peso_mercadoria * 43.21 + 25.00
taxa_ICMS = preco_parcial * 0.62
preco_total = preco_parcial + taxa_ICMS

#Dessa Forma
print(round(preco_total,2))
