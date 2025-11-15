import math
A = float(input())
B = float(input())
grau = float(input())
rad = math.radians (grau)
cc = math.sqrt(A**2 + B**2 - 2* A * B*math.cos(rad))
cc_rounded = round (cc,2)
print (cc_rounded)