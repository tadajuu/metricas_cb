# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.

# area e volume de formas geometricas

# 1 modulo

import math 

# 2 entrada

raio_r = float(input("5"))

# 3 comando

area = math.pi * raio_r ** 2

volume = (4 / 3) * math.pi * raio_r ** 3

# 4 saida

print(round(area, 3))

print(round(volume, 3))