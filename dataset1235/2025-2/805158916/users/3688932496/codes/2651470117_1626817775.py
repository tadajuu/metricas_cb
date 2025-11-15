# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
import math
# raio
r =  float (input("Digite o valor do raio :"))
# aréa do circulo 
area = math.pi * r **  2
#volume da esfera 
volume = (4/3) * math.pi * r ** 3
# saidas
print(round(area,3))
print(round(volume,3))