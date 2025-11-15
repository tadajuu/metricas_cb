nota1 = float(input("Insira a primeira nota:"))
nota2 = float(input("Insira a segunda nota:"))
nota3 = float(input("Insira a terceira nota:"))
nota4 = float(input("Insira a quarta nota:"))

mediap1 = (nota1 * 1) + (nota2 * 2) + (nota3 * 3) + (nota4 * 4)
mediap2 = mediap1 / (1+2+3+4)

print(round(mediap2,2))