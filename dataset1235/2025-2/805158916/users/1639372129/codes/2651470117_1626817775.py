# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
import math
raio = float(input("Escreva um numero: "))
AC  = math.pi*raio**2
VC = 4/3*math.pi*raio**3
print(round(AC, 3))
print(round(VC, 3))