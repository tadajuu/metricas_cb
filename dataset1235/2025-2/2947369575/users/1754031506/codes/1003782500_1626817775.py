# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
import math
X = float(input("raio r: "))

A = float(math.pi*X**2)
V = float(4/3*math.pi*X**3)

print(round(A,3))
print(round(V,3))