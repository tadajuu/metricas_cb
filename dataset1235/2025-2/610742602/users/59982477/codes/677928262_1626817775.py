import math 
#Lendo o raio 
raio = float(input())
#Calculando a área do círculo 
area_circulo = math.pi * raio ** 2 
#Calculando o volume da esfera 
volume_esfera = (4/3) * math.pi * raio ** 3
#Imprimendo os resultados  arredondados para 3 casas decimais 
print(round(area_circulo, 3))
print(round(volume_esfera, 3))