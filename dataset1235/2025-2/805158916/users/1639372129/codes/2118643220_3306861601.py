import math

# faça seu código aqui!
lado = float(input())
ap =  lado / (2*math.tan(math.pi/9))
area = 9/2*lado*ap
print(round(area, 2))