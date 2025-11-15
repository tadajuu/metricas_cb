import math 
pi = math.pi
tag = math.tan(pi/5)
# faça seu código aqui!
lado = float(input("Lado :"))
apotema = lado/(2*tag)
area = 5/2*lado*apotema
print(round(area, 2))