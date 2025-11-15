nota_1 = float(input("Qual a nota 1?: "))
nota_2 = float(input("Qual a nota 2?: "))
nota_3 = float(input("Qual a nota 3?: "))
nota_4 = float(input("Qual a nota 1?: "))

media_1 = nota_1 * 1
media_2 = nota_2 * 2
media_3 = nota_3 * 3
media_4 = nota_4 * 4

soma_nota = media_1 + media_2 + media_3 + media_4
soma_peso = 1 + 2 + 3 + 4

nota = soma_nota / soma_peso

print(round(nota, 2))