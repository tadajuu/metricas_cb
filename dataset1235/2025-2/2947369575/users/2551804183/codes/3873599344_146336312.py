# Total de moedas
moedas_total = 50
numero_guerreiros = 3

# Cálculo das moedas por guerreiro (divisão inteira)
moedas_por_guerreiro = moedas_total // numero_guerreiros

# Cálculo das moedas para o informante (resto da divisão)
moedas_informante = moedas_total % numero_guerreiros

# Impressão dos resultados
print(moedas_por_guerreiro)
print(moedas_informante)