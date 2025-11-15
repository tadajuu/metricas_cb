import math

# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.

raio = float(input("Valor do raio: "))

area = math.pi * raio**2
volume = (4/3) * math.pi * raio**3

print(round(area,3))
print(round(volume,3))
