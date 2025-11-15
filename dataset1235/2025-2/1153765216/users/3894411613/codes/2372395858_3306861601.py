import math

lado = float(input("Digite o comprimento: "))
apotema = lado / (2 * math.tan(math.pi / 9))
area = (9/2) * lado * apotema 

print(round(area , 2))