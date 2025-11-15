# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.

dist = float(input("Informe a distancia percorrida em km: "))
comb = float (input("Informe o total de combustível gasto em l: "))

consumo = dist/comb

print(round(consumo,3), "km/l")
