#notas 
nota1 = float(input(""))
nota2 = float(input(""))
nota3 = float(input(""))
nota4 = float(input(""))

#peso
peso1= 1
peso2 = 2
peso3= 3
peso4= 4
#peso total
pt = peso1+peso2+peso3+peso4

#notas com peso 
nt = nota1*peso1 + nota2*peso2 + nota3*peso3 + nota4*peso4

#media ponderada
media = (nt)/pt

# resultado
print(round(media,2))