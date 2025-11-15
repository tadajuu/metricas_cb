a= float(input("qual a distância entre você a primeira árvore?: "))
b= float(input("qual a distãncia entre você e  segunda árvore?: "))
c= float(input("qual o ângulo entre a e b em graus?: "))

import  math
              
ang=math.radians(c)
              
cs=math.cos(ang)
              
f=(a**2+b**2-2*a*b*cs)**0.5
              
print(round(f,2))
              