from math import *
# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
r = float(input("Insira o valor de um raio r: "))

area_circulo = pi * r**2
volume_esfera = 4/3 * pi * r**3

print(round(area_circulo, 3))
print(round(volume_esfera, 3))
