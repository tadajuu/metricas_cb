import math

T = 2*math.tan(math.pi/5)
Lado = float(input("Informe o lado do pentágono:"))
Area = 5*Lado**2/(2*T)
print(round(Area,2))