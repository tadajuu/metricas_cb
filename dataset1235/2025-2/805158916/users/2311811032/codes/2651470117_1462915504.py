# from math import *

# faça seu código aqui!

# Cálculo do Pentágono

# 1 Módulo matemático
import math

# 2 Entrada

lado = float(input('5.0'))

# 3 Cálculo da apótema
apotema = lado / (2 * math.tan(math.pi / 5))

# 4 Cálculo da área
area = (5/2) * lado * apotema 

# 5 Saída 
print(round(area, 2))