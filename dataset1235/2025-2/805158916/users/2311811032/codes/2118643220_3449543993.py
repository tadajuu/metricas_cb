# Área do Decágono

from math import *

# faça seu código aqui!

import math

# 1 Entrada
lado = float(input('25.0'))

# 2 Comando

# 2.1 Apótema
apotema = lado / (2 * math.tan(math.pi / 10))

# 2.2 Área
area = 5 * lado * apotema

# 3 Saída
print(round(area, 2))