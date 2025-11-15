# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.

import math

x = float(input("raio r: "))

y = float(math.pi*x**2)

z = float(4/3*math.pi*x**3)

print(round(y,3))
print(round(z,3))