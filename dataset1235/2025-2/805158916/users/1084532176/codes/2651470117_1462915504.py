from math import tan 
from math import pi 
L= float (input("escreva o lado do pentagono") )
p= L/(2*tan(pi/5))
a= (5/2)*L*p
print (round (a,2))