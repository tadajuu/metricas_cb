valor_estacionamento = 15 #por hora
taxa_fixa = 5

tempo_estacionado = float(input())
valor_inicial = (tempo_estacionado*valor_estacionamento) + taxa_fixa
valor_com_taxa = valor_inicial + (valor_inicial * 0.2)

print(round(valor_com_taxa, 2))