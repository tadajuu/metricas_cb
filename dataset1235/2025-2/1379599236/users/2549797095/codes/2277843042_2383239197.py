import math 
a = float(input("informe o lado a: "))
b = float(input("informe o lado b: "))
y = float(input("informe o angulo: "))
ang = float(math.radians(y))
c = print(round(math.sqrt(a**2 + b**2 - 2*a*b * math.cos(ang)),2))