# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.

from math import *

r = float(input("Informe o valor do raio: "))

areacirculo = pi * (r**2)
volumeesfera = (4/3) * pi * (r**3)

print(round(areacirculo,3))
print(round(volumeesfera,3)) 