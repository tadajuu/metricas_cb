import math
dist_a = float (input("Informe a distancia 'a': "))
dist_b = float (input("Informe a distancia 'b': "))
y = float(input("Informe o angulo 'y': "))
dist_c = math.sqrt((dist_a**2) + (dist_b**2)- 
(2* dist_a*dist_b*math.cos(math.radians(y))))
print(round(dist_c,2))
