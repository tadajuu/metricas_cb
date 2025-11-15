litros= float(input("Quantidade de litros abastecidos"))
Pg=2.86
Tl=50.00
valorC= litros * Pg
valorS = valorC+Tl
valorT=valorS* (1+34/100)
print(round(valorT, 2))