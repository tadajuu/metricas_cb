from math import *
lado = int( input( " comprimento do lado hexágono: "))
opotema = lado /( 2*tan(pi/6))
area = 3* lado * opotema 
print( round( area, 2))