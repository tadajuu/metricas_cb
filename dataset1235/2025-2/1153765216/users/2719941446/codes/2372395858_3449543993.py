import math
lado=float(input("LADO: "))

tans=2*math.tan(math.pi/10)
apot=lado/tans

area=5*lado*apot

print(round(area,2))

