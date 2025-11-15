from math import *
lado= float(input("comprimento do lado do pentagono: "))
opotema = lado / (2* tan(pi/5))
area= (5*lado*opotema) /2
print(round(area,2))