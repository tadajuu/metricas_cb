from math import *

# Values

distancia_A= float(input())
distancia_B= float(input())
angulo_A_B= float(input())

# Intermitum
angulo_A_B_radiano= radians(angulo_A_B)
distancia_entre_arvores= sqrt(distancia_A**2 + distancia_B**2 - (2*distancia_A*distancia_B*cos(angulo_A_B_radiano)))

# And So

print(round(distancia_entre_arvores,2))