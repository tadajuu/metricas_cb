# Leitura dos dados de entrada
tempo = float(input())
velocidade = float(input())

# Cálculo da distância percorrida
distancia = tempo * velocidade

# Cálculo do consumo de combustível
autonomia = 12.0
litros_usados = distancia / autonomia

# Exibição dos resultados
print(distancia)
print(litros_usados)
