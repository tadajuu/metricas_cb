#import math

from math import cos, radians, sqrt

# entrada
dist_a = float(input())
dist_b = float(input())
ang_c = float(input())

# processamento
soma = dist_a ** 2 + dist_b ** 2
cos = 2 * dist_a*dist_b*cos(radians(ang_c))

c = sqrt( (soma-cos) )

# saída
print(round(c, 2))
