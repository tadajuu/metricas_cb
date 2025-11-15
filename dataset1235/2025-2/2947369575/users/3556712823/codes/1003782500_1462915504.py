import math
lado = float (input("Qual o comprimento do lado do pentágono?"))
apotema = lado/(2*(math.tan(math.pi/5)))
A = (5/2)*lado*apotema

print(round(A,2))