from math import  tan , radians

#entrada
lado = float(input("Digite o comprimento do lado do pentagono:"))

# calculo da apótema
apotema = lado / (2 * tan(radians(36)))

# calculo da area
area = (5 * lado * apotema)/ 2

#saida formatada com duas casas decimais
print(f"A area do pentagono é {area:.2f}")