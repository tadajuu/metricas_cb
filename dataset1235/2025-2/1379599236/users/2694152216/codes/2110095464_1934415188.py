distancia = float(input("Digite a distancia percorrida (km): "))
combustivel = float(input("Digite o combustivel gasto (litros): "))

consumo_medio = distancia / combustivel

print(round(consumo_medio, 3), "km/l")