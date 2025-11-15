# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
from math import *

t1 = radians(float(input("T1 em graus: ")))
g1 = radians(float(input("G1 em graus: ")))
t2 = radians(float(input("T2 em graus: ")))
g2 = radians(float(input("G2 em graus: ")))

r = 6371.01

d = r*acos((sin(t1)*sin(t2))+(cos(t1)*cos(t2)*cos(g1-g2)))

print(round(d,2))