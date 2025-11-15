# Distância, Observador e Angulo

# 1 Módulo matemático
import math

# 2 Entrada
a = float(input('10'))
b = float(input('20'))
gama = float(input('30'))

# 3 Conversão de graus para radianos 
gama_rad = math.radians(gama)

# 4 Lei dos Cossenos 
c = math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(gama_rad))

# 5 saida
print(round(c, 2))