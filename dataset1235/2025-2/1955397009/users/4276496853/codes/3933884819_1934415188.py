# Leitura da distância total percorrida (em km)
distancia = float(input())

# Leitura do total de combustível gasto (em litros)
combustivel = float(input())

# Cálculo do consumo médio
consumo_medio = distancia / combustivel

# Impressão do consumo médio com até 3 casas decimais, seguido de "km/l"
print(round(consumo_medio, 3), "km/l")
