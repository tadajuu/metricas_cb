# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.import math
from math import *
area_r = float(input())
calculo_r = pi * (area_r**2)
calculo_a = (4/3) * pi * (area_r**3)
print(round(calculo_r, 3))
print(round(calculo_a, 3))