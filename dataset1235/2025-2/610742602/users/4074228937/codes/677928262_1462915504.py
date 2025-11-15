import math

x = float(input("Insira o comprimento do lado do pentágono: "))

area = 5/2 * x * (x/(2* math.tan((math.pi)/5)))

print(round(area, 2))