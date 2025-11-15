# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
import math
raio = float(input("Digite o valor do raio"))
area_circulo = math.pi * raio ** 2
volume_esfera = ((4 / 3) * math.pi * raio ** 3)
print(round(area_circulo, 3))
print(round(volume_esfera, 3))