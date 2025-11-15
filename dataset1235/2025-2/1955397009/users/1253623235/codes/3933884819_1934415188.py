# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
dist = float(input("Distancia total percorrida: "))
cobus = float(input("Combustivel gasto: "))
cm = dist / cobus
x = round(cm, 3)
print(f" {x} km/l")