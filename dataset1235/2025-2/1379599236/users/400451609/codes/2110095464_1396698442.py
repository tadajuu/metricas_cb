import math

x_a = float(input("Qual o valor de Xa? "))
y_a = float(input("Qual o valor de Ya? "))
x_b = float(input("Qual o valor de Xb? "))
y_b = float(input("Qual o valor de Yb? "))

dist = math.sqrt((x_b-x_a)**2 + (y_b-y_a)**2)

print(round(dist,3))