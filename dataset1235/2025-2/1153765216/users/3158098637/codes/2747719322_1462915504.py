import math
l = float(input("comprimento do lado: "))
apotema = l/(2*math.tan(math.pi/5))
area = round((5/2*l*apotema),2)
print(area)