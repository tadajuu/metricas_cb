# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
import math
r= float(input("digite um valor para o raio:"))
A= math.pi * (r** 2)
V= math.pi * (4/3) * (r** 3)

print(round(A, 3))
print(round(V, 3))