import math
A = float(input())
B = float(input())
Y = float(input())
Y1 = math.radians(Y)
D = math.sqrt(A**2 + B**2 - 2*A*B*math.cos(Y1))
print (round(D, 2))