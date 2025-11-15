import math 
#Lendo as entradas 
a = float(input())
b = float(input())
gamma_graus = float(input())

#Convertendo o ângulo de graus para radianos
gamma_rad = math.radians(gamma_graus)

#Calculando a distancia usando a lei dos cossenos 
c = math.sqrt(a**2 + b**2 - 2*a*b*math.cos(gamma_rad))

#Imprimindo a distância com 2 casas decimais
print(round(c, 2))