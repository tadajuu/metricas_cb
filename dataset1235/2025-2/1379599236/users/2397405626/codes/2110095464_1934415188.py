# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.

distancia = float(input("Digite a distancia percorrida em KM: "))
combustivel = float(input("Informe quantos litros de combustivel foram gastos: "))
consumo = distancia/combustivel

print(round(consumo,3),"km/l")