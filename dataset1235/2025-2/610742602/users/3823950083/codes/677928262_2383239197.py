import math
dist_a = float(input("Informe a distancia 'a': "))
dist_b = float(input("Informe a distancia 'b': "))
Y = float(input("Informe o ângulo 'Y': "))

dist_c = math.sqrt((dist_a**2) + (dist_b**2) - 
                   (2*dist_a*dist_b * math.cos(math.radians(Y))))

print (round(dist_c,2))

                   