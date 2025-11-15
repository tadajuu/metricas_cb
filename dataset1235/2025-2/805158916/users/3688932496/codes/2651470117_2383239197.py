import math
#entradas das distâncias e dos ângulos( em graus)
a = float (input("Informe a distância A:"))
print("")
b = float (input("Informea distância B:"))
print("")
g = float (input("Informe o grau:"))
print("")
 # de angulos para radianos
g_rad = math.radians(g)
# leis dos cossenos
cc = math.sqrt(a **2 + b **2 - 2 * a * b * math.cos(g_rad))
print(round(cc,2))