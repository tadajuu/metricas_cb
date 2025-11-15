nota_um = float(input("digite um numero: "))
nota_dois = float(input("digite um valor: "))
nota_tres = float(input("digite um valor: "))
nota_quatro = float(input("digite um valor: "))
#peso das notas
p1 , p2, p3, p4 = 1, 2, 3, 4
#calculo da media
media = (nota_um * p1 + nota_dois * p2 + nota_tres * p3 + nota_quatro * p4) / (p1 + p2 + p3 + p4)
print(round(media, 2))