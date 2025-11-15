distanciaP = float(input("Distancia percorrida: "))
cg = float(input("combustivel gasto: "))
consumo = distanciaP / cg
consumo_arredondado = round(consumo, 3)

print(f" {consumo_arredondado} km/l")