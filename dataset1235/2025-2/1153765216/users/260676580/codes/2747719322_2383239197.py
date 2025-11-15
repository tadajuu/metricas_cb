import math
a=float(input("digite a distancia a: "))
b=float(input("digite a distancia b:"))
y_graus = float(input("Digite o angulo y em graus:"))
y_radianos =math.radians(y_graus)
c=math.sqrt(a**2+b**2-2*a*b*math.cos(y_radianos))
print(f"A distancia entre as arvores e:{c:.2f}")
