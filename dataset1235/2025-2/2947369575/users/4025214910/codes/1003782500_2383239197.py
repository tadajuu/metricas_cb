a= float(input("Qual a distância entre você e a primeira àrvore?: "))
b= float(input("Qual a distãncia entre você e a segunda àrvore?: "))
c= float(input("Qual o ângulo entre a e b, em graus?:"))
import math
ang=math.radians(c)
cs= math.cos(ang)
f= (a**2+b**2-2*a*b*cs)**0.5
print(round(f,2))