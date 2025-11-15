a= float(input("qual a distancia entre você e a primeira arvore?: "))
b= float(input("qual a distancia entre você e a segunda arvore?: "))
c= float(input("qual o angulo entre a e b em graus?: "))
import math
ang=math.radians(c)
cs= math.cos(ang)
f= (a**2+b**2-2*a*b*cs)**0.5
print(round(f,2))
