# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.

dist = float(input("Km rodados: "))
comb = float(input("Combustível: "))

consumo = dist/comb

print(round(consumo, 3), "km/l")