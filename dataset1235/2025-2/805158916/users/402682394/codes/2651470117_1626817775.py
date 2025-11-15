import math

R = float(input("Informe o raio:"))

Area = math.pi*R**2
Vol = 4/3*math.pi*R**3

print(round(Area,3))
print(round(Vol,3))