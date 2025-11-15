from math import *

#In
lado_pentagono= float(input())

#Intermission
apotema= lado_pentagono/(2*tan(pi/5))
area= 5/2*lado_pentagono*apotema

#Out
print(round(area,2))