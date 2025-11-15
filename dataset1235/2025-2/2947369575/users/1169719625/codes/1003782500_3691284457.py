nota1 = float(input())
nota2 = float(input())
nota3 = float(input())
nota4 = float(input())

peso1, peso2, peso3, peso4 = 1, 2, 3, 4

media_ponderada = ( nota1*peso1 + nota2*peso2 + nota3*peso3 + nota4*peso4) / (peso1 + peso2  + peso3 + peso4)

print(round(media_ponderada, 2))

