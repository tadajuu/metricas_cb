import math
distA = float(input("Qual a distância entre o observador e a primeira árvore?"))
distB = float(input("Qual a distância entre o observador e a segunda árvore?"))
angulo = float (input("Qual o angulo em graus Y entre a e b? "))

cos = math.cos(math.radians(angulo))

c= math.sqrt((distA**2)+(distB**2) - 2*distA*distB*cos)
print(round(c, 2))