# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.

import math

R = float(input("Digite um Raio: "))
area = round(math.pi * R**2, 3) 
volume = (4*math.pi*R**3)/3
print(round(area, 3))
print(round(volume, 3))
