import math 
#Lendo o comprimento do lado do pentágono 
lado = float(input())
#Calculando a apótema 
apotema  = lado / (2 * math.tan(math.pi/5))
#Calculando a área do pentágono 
area = (5 * lado * apotema)/2
#Imprimindo a área arredondada para 2 casas decimais 
print(round(area,2))