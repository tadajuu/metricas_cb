# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
import math
r = float(input("Insira o valor do raio: "))
#Área
A = math.pi * r**2
#Volume
V = (4/3) * math.pi * r**3
#Impressão dos resultados
print(round(A,3))
print(round(V,3))